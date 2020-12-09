import re

def read_passports(data):
    return [{kv[0]: kv[1] for kv in re.findall(r"([a-z]{3}):(\S+)", p)}
            for p in data.split("\n\n")]

def required_fields(p):
    return p.keys() >= {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}

def height_ok(hgt):
    h, unit = int(hgt[:-2]), hgt[-2:]
    if   unit == 'cm': return 150 <= h <= 193
    elif unit == 'in': return 59 <= h <= 76
    else: return False

def valid(p):
    return (required_fields(p)
        and 1920 <= int(p['byr']) <= 2002
        and 2010 <= int(p['iyr']) <= 2020
        and 2020 <= int(p['eyr']) <= 2030
        and height_ok(p['hgt'])
        and re.match(r"^#[0-9a-f]{6}$", p['hcl'])
        and p['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        and re.match(r"^\d{9}$", p['pid']))

with open("day04.txt", "r") as fh:
    passports = read_passports(fh.read())
    print("2020 day 04 part 1: %d" % len([p for p in passports if required_fields(p)]))
    print("2020 day 04 part 1: %d" % len([p for p in passports if valid(p)]))

