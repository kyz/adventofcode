import functools, operator

def hex2bin(s):
    return ("{0:0" + str(len(s) * 4) + "b}").format(int(s, 16))

def decode(packet):
    version, typeid = int(packet[0:3], 2), int(packet[3:6], 2)
    if typeid == 4: # literal value
        value, pos, keep_reading = 0, 6, True
        while keep_reading:
            keep_reading = packet[pos] == "1"
            value = (value << 4) | int(packet[pos+1:pos+5], 2)
            pos += 5
    else: # operator
        if packet[6] == "0": # sub packets by length
            value, pos, end = [], 22, 22 + int(packet[7:22], 2)
            while pos < end:
                value.append(decode(packet[pos:]))
                pos += value[-1][0]
        else: # sub packets by count
            value, pos = [], 18
            for i in range(int(packet[7:18], 2)):
                value.append(decode(packet[pos:]))
                pos += value[-1][0]
    return pos, version, typeid, value

def version_sum(packet):
    pos, version, typeid, value = packet
    return version + (sum(version_sum(p) for p in value) if type(value) == list else 0)

def evaluate(packet):
    pos, version, typeid, value = packet
    if   typeid == 0: return sum(evaluate(p) for p in value)
    elif typeid == 1: return functools.reduce(operator.mul, (evaluate(p) for p in value))
    elif typeid == 2: return min(evaluate(p) for p in value)
    elif typeid == 3: return max(evaluate(p) for p in value)
    elif typeid == 4: return value
    elif typeid == 5: return 1 if evaluate(value[0]) >  evaluate(value[1]) else 0
    elif typeid == 6: return 1 if evaluate(value[0]) <  evaluate(value[1]) else 0
    elif typeid == 7: return 1 if evaluate(value[0]) == evaluate(value[1]) else 0

with open("day16.txt", "r") as fh:
    packet = decode(hex2bin(fh.readline().strip()))
    print("2021 day 16 part 1: %d" % version_sum(packet))
    print("2021 day 16 part 2: %d" % evaluate(packet))

