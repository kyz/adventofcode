import collections, re

def read_rooms(fh):
    p = re.compile(r'([a-z-]+)-(\d+)\[([a-z]{5})\]')
    return [p.match(line).groups() for line in fh]

def real_room(room):
    c = collections.Counter(room[0])
    cksum = "".join(x for x in sorted(c, key=lambda x:(-c[x], x)) if x != "-")
    return room[2] == cksum[:5]

def decrypt(rooms):
    s = "abcdefghijklmnopqrstuvwxyz"
    for room in rooms:
        shift = int(room[1])
        decoder = {s[i]: s[(i + shift) % len(s)] for i in range(len(s))}
        name = "".join(decoder[c] for c in room[0] if c != '-')
        if name == "northpoleobjectstorage":
            return shift

with open("day04.txt", "r") as fh:
    rooms = [room for room in read_rooms(fh) if real_room(room)]
    print("2016 day 04 part 1: %d" % sum(int(room[1]) for room in rooms))
    print("2016 day 04 part 2: %d" % decrypt(rooms))

