def count_good_passwords(passwords, transform):
    return sum([1 if good_password(p, transform) else 0 for p in passwords])

def good_password(password, transform=None):
    seen = set()
    for word in password.split():
        word = transform(word)
        if word in seen:
            return False
        seen.add(word)
    return True

with open("day04.txt") as f:
    data = [line for line in f]
    identity = lambda s: s
    anagram = lambda s: "".join(sorted(s))
    print("2017 day 4 part 1: %d" % count_good_passwords(data, identity))
    print("2017 day 4 part 2: %d" % count_good_passwords(data, anagram))
