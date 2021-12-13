def process(program):
    pixels = set()
    for line in program:
        if line[:5] == "rect ":
            w, h = [int(n) for n in line[5:].split("x")]
            pixels |= {(x,y) for x in range(w) for y in range(h)}
        elif line[:13] == "rotate row y=":
            a, b = [int(n) for n in line[13:].split(" by ")]
            pixels = {((p[0] + b) % 50, p[1]) if p[1] == a else p for p in pixels}
        elif line[:16] == "rotate column x=":
            a, b = [int(n) for n in line[16:].split(" by ")]
            pixels = {(p[0], (p[1] + b) % 6) if p[0] == a else p for p in pixels}
    return pixels

def show(pixels):
    for y in range(6):
        print("".join("#" if (x,y) in pixels else " " for x in range(50)))

with open("day08.txt", "r") as fh:
    program = [line.strip() for line in fh]
    pixels = process(program)
    print("2016 day 08 part 1: %d" % len(pixels))
    print("2016 day 08 part 2:"); show(pixels)

