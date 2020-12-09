from operator import and_, or_, lshift, rshift

ops = {"AND": and_, "OR": or_, "LSHIFT": lshift, "RSHIFT": rshift}
env = dict()

def eval(var):
    if var[0].isdigit():
        return int(var)
    val = env[var]
    if type(val) == int:
        return val
    if   len(val) == 1: # x
        val = eval(val[0])
    elif len(val) == 2: # NOT x
        val = 65535 - eval(val[1])
    else: # x OP y
        val = ops[val[1]](eval(val[0]), eval(val[2]))
    env[var] = val
    return val

with open("day07.txt") as fh:
    data = [line.strip().split() for line in fh]
    for p in data:
        env[p[-1]] = p[:-2]
    print("2015 day 7 part 1: %d" % eval("a"))

    # reload program and set "b" to value computed for "a"
    b = [str(eval("a"))]
    for p in data:
        env[p[-1]] = p[:-2]
    env["b"] = b
    print("2015 day 7 part 2: %d" % eval("a"))
