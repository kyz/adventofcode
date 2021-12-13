import re

hyper_p = re.compile(r"\[([^]]+)\]")
abba_p = re.compile(r"([a-z])([a-z])\2\1")
aba_p = re.compile(r"(?=([a-z])([a-z])\1)")

def has_abba(ip):
    return [1 for abba in abba_p.findall(ip) if abba[0] != abba[1]]

def supports_tls(ip):
    return has_abba(ip) and not [1 for h in hyper_p.findall(ip) if has_abba(h)]

def supports_ssl(ip):
    hypers = hyper_p.findall(ip)
    supers = hyper_p.sub(" ", ip)
    for aba in aba_p.findall(supers):
        if aba[0] != aba[1]:
            bab = aba[1] + aba[0] + aba[1]
            for h in hypers:
                if bab in h:
                    return True
    return False

with open("day07.txt", "r") as fh:
    ips = [line.strip() for line in fh.readlines()]
    print("2016 day 07 part 1: %d" % sum(1 for ip in ips if supports_tls(ip)))
    print("2016 day 07 part 2: %d" % sum(1 for ip in ips if supports_ssl(ip)))
