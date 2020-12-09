from collections import defaultdict, deque

def run(program, pid, inq, outq):
    regs = defaultdict(int)
    regs["p"] = pid
    val = lambda n: regs[n] if n.isalpha() else int(n)
    ip = 0
    while ip >= 0 and ip < len(program):
        op, x, y = (program[ip] + " ?").split()[0:3]
        if   op == "set": regs[x]  = val(y)
        elif op == "add": regs[x] += val(y)
        elif op == "mul": regs[x] *= val(y)
        elif op == "mod": regs[x] %= val(y)
        elif op == "jgz" and val(x) > 0:
            ip += val(y) - 1
        elif op == "snd":
            outq.appendleft(val(x))
            yield "sent"
        elif op == "rcv":
            if inq:
                regs[x] = inq.pop()
                yield "rcvd"
            else:
                yield "wait"
        ip += 1

def part1(program):
    q = deque()
    for s0 in run(program, 0, q, q):
        if s0 == "rcvd":
            return q[0] # most recently sent value

def part2(program):
    q0, q1 = deque(), deque()
    p0 = run(program, 0, q0, q1)
    p1 = run(program, 1, q1, q0)
    count = 0
    while True:
        s0, s1 = next(p0), next(p1)
        if s1 == "sent":
            count += 1
        elif s0 == "wait" and s1 == "wait":
            return count

with open("day18.txt") as f:
    data = [line.strip() for line in f]
    print("2017 day 18 part 1: %d" % part1(data))
    print("2017 day 18 part 2: %d" % part2(data))
