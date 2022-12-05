def run(program, c):
    pc, regs = 0, {"a": 0, "b": 0, "c": c, "d": 0}
    rval = lambda x: regs[x] if x in regs else int(x)
    while pc < len(program):
        instr = program[pc]
        op, reg = instr[0:2]
        if   op == "cpy": regs[instr[2]] = rval(reg)
        elif op == "inc": regs[reg] += 1
        elif op == "dec": regs[reg] -= 1
        elif op == "jnz": pc += int(instr[2])-1 if rval(reg) != 0 else 0
        pc += 1
    return regs["a"]

with open("day12.txt", "r") as fh:
    program = [line.strip().split() for line in fh]
    print("2016 day 12 part 1: %d" % run(program, 0))
    print("2016 day 12 part 2: %d" % run(program, 1))

