import re

def read_instructions(fh):
    re1 = re.compile((r"(turn on|turn off|toggle) "
                      r"(\d+),(\d+) through (\d+),(\d+)"))
    return [re1.match(line).groups() for line in fh]

def count_lights(instructions, actions):
    lights = [[0] * 1000 for x in range(1000)]
    for i in instructions:
        action = actions[i[0]]
        sx, sy = int(i[1]), int(i[2]) + 1
        ex, ey = int(i[3]), int(i[4]) + 1
        for x in range(sx, ex):
            for y in range(sy, ey):
                lights[x][y] = action[lights[x][y]]
    return sum(sum(l) for l in lights)

with open("day06.txt") as fh:
    instructions = read_instructions(fh)
    onoff = {
        "turn on":  [1, 1],
        "turn off": [0, 0],
        "toggle":   [1, 0]
    }
    dimmable = {
        "turn on":  [x + 1         for x in range(50)],
        "turn off": [max(x - 1, 0) for x in range(50)],
        "toggle":   [x + 2         for x in range(50)]
    }
    print("2015 day 6 part 1: %d" % count_lights(instructions, onoff))
    print("2015 day 6 part 2: %d" % count_lights(instructions, dimmable))
