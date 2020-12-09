def run(program):
    ip, a, seen = 0, 0, set()
    while ip not in seen and ip < len(program):
        seen.add(ip)
        op, arg = program[ip]
        if   op == "acc": a += int(arg)
        elif op == "jmp": ip += int(arg) - 1
        ip += 1
    return ('loop' if ip in seen else 'ended', a)

def make_terminate(program):
    for p in program:
        if p[0] == "nop" or p[0] == "jmp":
            old = p[0]
            p[0] = "jmp" if old == "nop" else "nop"
            reason, a = run(program)
            if reason == 'ended':
                return a
            p[0] = old

with open("day08.txt", "r") as fh:
    program = [line.split(" ") for line in fh.readlines()]
    print("2020 day 08 part 1: %d" % run(program)[1])
    print("2020 day 08 part 2: %d" % make_terminate(program))
