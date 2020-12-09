data = "hepxcrrq"

def password(s):
    return [ord(c) - ord("a") for c in s]

def password_str(p):
    return "".join([chr(c + ord("a")) for c in p])

def inc_password(p):
    for i in reversed(range(8)):
        if p[i] < 25:
            p[i] += 1
            break
        p[i] = 0

def has_straight(p):
    for i in range(5):
        if p[i]+2 == p[i+1]+1 == p[i+2]:
            return True
    return False

def has_no_iol(p):
    for i in range(8):
        if p[i] == 8 or p[i] == 11 or p[i] == 14:
            return False
    return True

def has_two_pairs(p):
    return len(set([p[i] for i in range(7) if p[i] == p[i+1]])) >= 2

p = password(data)
while not (has_straight(p) and has_no_iol(p) and has_two_pairs(p)):
    inc_password(p)
print("2015 day 11 part 1: %s" % password_str(p))

inc_password(p)
while not (has_straight(p) and has_no_iol(p) and has_two_pairs(p)):
    inc_password(p)
print("2015 day 11 part 2: %s" % password_str(p))
