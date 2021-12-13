def read_map(fh):
    emap = {}
    for y, line in enumerate(fh):
        for x, h in enumerate(line.strip()):
            emap[x,y] = int(h)
    return emap

def neighbours(emap, k):
    return [n for n in [(k[0]-1,k[1]-1), (k[0],k[1]-1), (k[0]+1,k[1]-1),
                        (k[0]-1,k[1]+0),                (k[0]+1,k[1]+0),
                        (k[0]-1,k[1]+1), (k[0],k[1]+1), (k[0]+1,k[1]+1)] if n in emap]

def process_step(emap):
    flashed = set()
    for k in emap:
        emap[k] += 1
    while True:
        will_flash = {k for k in emap if emap[k] > 9 and k not in flashed}
        if not will_flash:
            break
        for k in will_flash:
            for n in neighbours(emap, k):
                emap[n] += 1
        flashed |= will_flash
    for k in flashed:
        emap[k] = 0
    return len(flashed)

def count_flashes(emap):
    flashes = 0
    for step in range(100):
        flashes += process_step(emap)
    return flashes

def all_flashed(emap):
    step = 1
    while process_step(emap) != 100:
        step += 1
    return step

with open("day11.txt", "r") as fh:
    emap = read_map(fh)
    print("2021 day 11 part 1: %d" % count_flashes(emap.copy()))
    print("2021 day 11 part 2: %d" % all_flashed(emap.copy()))

