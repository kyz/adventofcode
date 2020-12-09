def build_rules(data):
    rules = {}
    for line in data:
        key, rule = line.split(" => ")
        for i in range(4):
            vflip = "/".join(reversed(key.split("/")))
            hflip = "/".join([x[::-1] for x in key.split("/")])
            rules[key] = rules[vflip] = rules[hflip] = rule
            rotate = [1,4,2,0,3] if len(key) == 5 else [2,6,10,3,1,5,9,7,0,4,8]
            key = "".join([key[i] for i in rotate]) # rotate square 90 degrees
    return rules

def enhance(picture, rules):
    out = []
    skip = 2 if len(picture) % 2 == 0 else 3
    for y in range(0, len(picture), skip):
        lines = [""] * (skip + 1)
        for x in range(0, len(picture), skip):
            blk = "/".join([picture[y+i][x:x+skip] for i in range(skip)])
            for i, nl in enumerate(rules[blk].split("/")):
                lines[i] += nl
        out.extend(lines)
    return out

def count_pixels(picture):
    return sum([line.count("#") for line in picture])

with open("day21.txt") as f:
    data = [line.strip() for line in f.readlines()]
    rules = build_rules(data)
    picture = [".#.", "..#", "###"]
    for i in range(5): picture = enhance(picture, rules)
    print("2017 day 21 part 1: %d" % count_pixels(picture))
    for i in range(18-5): picture = enhance(picture, rules)
    print("2017 day 21 part 2: %d" % count_pixels(picture))
