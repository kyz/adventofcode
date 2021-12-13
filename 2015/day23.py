def run(program, a):
    pc, regs = 0, {"a": a, "b": 0}
    while pc < len(program):
        instr = program[pc]
        op, reg = instr[0], instr[1][0]
        if   op == "hlf": regs[reg] //= 2
        elif op == "tpl": regs[reg] *= 3
        elif op == "inc": regs[reg] += 1
        elif op == "jmp": pc += int(instr[1]) - 1
        elif op == "jie" and regs[reg] & 1 == 0: pc += int(instr[2]) - 1
        elif op == "jio" and regs[reg] == 1:     pc += int(instr[2]) - 1
        pc += 1
    return regs["b"]
        

with open("day23.txt", "r") as fh:
    program = [line.split() for line in fh]
    print("2015 day 23 part 1: %d" % run(program, 0))
    print("2015 day 23 part 2: %d" % run(program, 1))

