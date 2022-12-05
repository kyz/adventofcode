#!/usr/bin/env python3
import base64, itertools, os, re, struct, urllib.request
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def download_onion():
    if os.path.exists("onion.txt"):
        with open("onion.txt", "r") as fh:
            layer0 = fh.read()
    else:
        req = urllib.request.Request("https://www.tomdalling.com/toms-data-onion/",
                                     headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            layer0 = resp.read().decode('UTF-8')
            with open("onion.txt", "w") as fh:
                fh.write(layer0)
    return (layer0.replace("&quot;", '"')
                  .replace("&#39;", "'")
                  .replace("&lt;", "<")
                  .replace("&gt;", ">")
                  .replace("&amp;", "&"))

def extract_payload(data):
    data = re.search(r'<~.+~>', data, re.DOTALL).group()
    return base64.a85decode(data, adobe=True)

def process_layer1(data):
    ror = lambda x: (x >> 1) | ((x << 7) & 0x80)
    flip_and_rotate = [ror(x ^ 0x55) for x in range(256)]
    return bytes(flip_and_rotate[b] for b in data)

def process_layer2(data):
    parity_ok = [(x.bit_count() & 1) == 0 for x in range(256)]
    p_ok = ((b >> 1) for b in data if parity_ok[b])
    out = list()
    for p in zip(p_ok, p_ok, p_ok, p_ok, p_ok, p_ok, p_ok, p_ok):
        a = ((p[0] << 49) | (p[1] << 42) | (p[2] << 35) | (p[3] << 28) |
             (p[4] << 21) | (p[5] << 14) | (p[6] << 7)  | p[7])
        out += [(a >> 48) & 0xFF, (a >> 40) & 0xFF, (a >> 32) & 0xFF,
                (a >> 24) & 0xFF, (a >> 16) & 0xFF, (a >> 8) & 0xFF, a & 0xFF]
    return bytes(out)

# it's known the output begins "==[ Layer 4/6: " by convention so far.
# it's also known the next 32 bytes will have a horizontal rule made of "="s,
# so if we assume the unknown plaintext is "="x16, it will XOR with the "="s
# in the following 32 bytes and reveal the true plaintext, "Network Traffic ]"
def process_layer3(data):
    plaintext = bytes("==[ Layer 4/6: Network Traffic ]", "ASCII")
    key = [data[i] ^ plaintext[i] for i in range(32)]
    return bytes(data[i] ^ key[i & 0x1F] for i in range(len(data)))

def process_layer4(data):
    IPv4_20b, UDP, SRC, DEST, PORT = 0x45, 17, 0x0A01010A, 0x0A0101C8, 42069
    def ip_sum_ok(data):
        cksum = sum((data[i] << 8) | data[i+1] for i in range(0, len(data), 2))
        return ((cksum & 0xFFFF) + (cksum >> 16)) == 0xFFFF
    def udp_sum_ok(data):
        data = data[0:8] + bytes([0, UDP]) + data[12:14] + data[8:]
        if len(data) & 1: data += bytes([0])
        return ip_sum_ok(data)

    out = bytes()
    pos = 0
    while pos+28 < len(data):
        h = struct.unpack('>BBHHHBBHIIHHHH', data[pos:pos+28])
        if h[0] == IPv4_20b and h[6] == UDP and h[8] == SRC and h[9] == DEST and h[11] == PORT:
            if ip_sum_ok(data[pos:pos+20]) and udp_sum_ok(data[pos+12:pos+20+h[12]]):
                out += data[pos+28:pos+20+h[12]]
        pos += h[2]
    return out

def process_layer5(data):
    # cryptography.hazmat.primitives.keywrap.aes_key_unwrap() rejects the custom IV
    # so we need to copy/paste its implementation and tweak it
    d = Cipher(algorithms.AES(data[0:32]), modes.ECB()).decryptor()
    r = [data[i : i + 8] for i in range(40, 80, 8)]
    a = r.pop(0)
    n = len(r)
    for j in reversed(range(6)):
        for i in reversed(range(n)):
            atr = (
                int.from_bytes(a, byteorder="big") ^ ((n * j) + i + 1)
            ).to_bytes(length=8, byteorder="big") + r[i]
            b = d.update(atr)
            a = b[:8]
            r[i] = b[-8:]
    unwrapped_key = b"".join(r)

    # now it's straightforward to decode with the unwrapped key, IV, data
    d = Cipher(algorithms.AES(unwrapped_key), modes.CTR(data[80:96])).decryptor()
    return d.update(data[96:]) + d.finalize()

def process_layer6(data):
    data = list(data) # convert bytes to list to allow writing
    rb = [0, 0, 0, 0, 0, 0] # a,b,c,d,e,f (8-bit)
    rl = [0, 0, 0, 0 ,0 ,0] # la,lb,lc,ld,ptr,pc (32-bit)
    out = [] # output stream
    read_le32 = lambda x: data[x] | (data[x+1] << 8) | (data[x+2] << 16) | (data[x+3] << 24)
    while True:
        i = data[rl[5]]; rl[5] += 1
        if i == 0x01: return bytes(out)
        elif i == 0x02: out.append(rb[0])
        elif i == 0x21 or i == 0x22:
            rl[5] = read_le32(rl[5]) if (rb[5] != 0 if i == 0x22 else rb[5] == 0) else rl[5] + 4
        elif i >= 0x40 and i < 0x80: # MV / MVI
            sreg, dreg = i & 0x07, (i >> 3) & 0x07
            if sreg == 0: # MVI
                src = data[rl[5]]; rl[5] += 1
            elif sreg < 7: # MV ,a-f
                src = rb[sreg-1]
            else: # MV ,(ptr+c)
                src = data[rl[4] + rb[2]]
            if dreg == 7: data[rl[4] + rb[2]] = src
            else:         rb[dreg-1] = src
        elif i >= 0x80 and i < 0xC0: # MV32 / MVI32
            sreg, dreg = i & 0x07, (i >> 3) & 0x07
            if sreg == 0:
                rl[5] += 4
                rl[dreg-1] = read_le32(rl[5]-4)
            else:
                rl[dreg-1] = rl[sreg-1]
        elif i == 0xC1: rb[5] = 0 if rb[0] == rb[1] else 1
        elif i == 0xC2: rb[0] = (rb[0] + rb[1]) & 0xFF
        elif i == 0xC3: rb[0] = (rb[0] - rb[1]) & 0xFF
        elif i == 0xC4: rb[0] = rb[0] ^ rb[1]
        elif i == 0xE1: rl[4] += data[rl[5]]; rl[5] += 1

layer0 = download_onion()
layer1 = extract_payload(layer0).decode('UTF-8')
layer2 = process_layer1(extract_payload(layer1)).decode('UTF-8')
layer3 = process_layer2(extract_payload(layer2)).decode('UTF-8')
layer4 = process_layer3(extract_payload(layer3)).decode('UTF-8')
layer5 = process_layer4(extract_payload(layer4)).decode('UTF-8')
layer6 = process_layer5(extract_payload(layer5)).decode('UTF-8')
layer7 = process_layer6(extract_payload(layer6)).decode('UTF-8')
print(layer7)
