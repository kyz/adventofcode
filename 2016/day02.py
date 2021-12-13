pad1 = {     (0,0): "1", (1,0): "2", (2,0): "3",
             (0,1): "4", (1,1): "5", (2,1): "6",
             (0,2): "7", (1,2): "8", (2,2): "9"}
pad2 = {                 (2,0): "1",
             (1,1): "2", (2,1): "3", (3,1): "4",
 (0,2): "5", (1,2): "6", (2,2): "7", (3,2): "8", (4,2): "9",
             (1,3): "A", (2,3): "B", (3,3): "C",
                         (2,4): "D"}

def keypad(instructions, pad, x, y):
    moves = {"U":(0,-1), "D": (0,1), "L":(-1,0), "R":(1,0)}
    code = ""
    for inst in instructions:
        for i in inst:
            dx = x + moves[i][0]
            dy = y + moves[i][1]
            if (dx, y) in pad: x = dx
            if (dy, x) in pad: y = dy
        code += pad[x,y]
    return code

with open("day02.txt", "r") as fh:
    instructions = [line.strip() for line in fh]
    print("2016 day 02 part 1: %s" % keypad(instructions, pad1, 1, 1))
    print("2016 day 02 part 2: %s" % keypad(instructions, pad2, 0, 2))
