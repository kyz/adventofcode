import intcode

def breakout_demo(p):
    cpu = intcode.computer(p)
    screen = dict()
    while True:
        try:
            x, y, tile = next(cpu), next(cpu), next(cpu)
            screen[x, y] = tile
        except StopIteration:
            return bricks_remaining(screen)

def breakout(p):
    p[0] = 2
    cpu = intcode.computer(p)
    screen = dict()
    joystick, paddle, ball = 0, None, None
    #print("\033[2J")
    while True:
        x = next(cpu)
        if x is None: x = cpu.send(joystick)
        y = next(cpu)
        tile = next(cpu)
        screen[x,y] = tile
        if x == -1 and y == 0 and bricks_remaining(screen) == 0:
            return tile # final score
        elif tile == 3:
            paddle = x
        elif tile == 4:
            ball = x
        if paddle is not None and ball is not None:
            joystick = -1 if ball < paddle else 1 if ball > paddle else 0
        #print("\033[H Score: %d" % screen.get((-1,0), 0))
        #for y in range(20):
        #    print("".join([" #.=O"[screen.get((x,y), 0)] for x in range(40)]))

def bricks_remaining(screen):
    return len([1 for x in screen if screen[x] == 2])

with open("day13.txt") as fh:
    p = [int(c) for c in fh.readline().split(",")]
    print("2019 day 13 part 1: %d" % breakout_demo(p))
    print("2019 day 13 part 2: %d" % breakout(p))
