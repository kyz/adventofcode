def run(program):
    regs = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0}
    val = lambda n: regs[n] if n.isalpha() else int(n)
    ip, muls = 0, 0
    while ip >= 0 and ip < len(program):
        op, x, y = (program[ip] + " ?").split()[0:3]
        if   op == "set": regs[x]  = val(y)
        elif op == "sub": regs[x] -= val(y)
        elif op == "mul": regs[x] *= val(y); muls += 1
        elif op == "jnz" and val(x) != 0:
            ip += val(y) - 1
        ip += 1
    return muls

with open("day23.txt") as f:
    data = [line.strip() for line in f]
    print("2017 day 23 part 1: %d" % run(data))

    """program with a=1 is equivalent to:
       int h = 0;
       for (int b = 108100; b < 125100; b += 17) {
           int f = 1;
           for (int d = 2; d < b; d++) {
               for (int e = 2; e < b; e++) {
                   if ((d * e) == b) f = 0;
	       }
           }
           if (f == 0) h++;
       }
       which is equivalent to: how many numbers, from 108100 to 125100 (included), stepping 17 at a time, are NOT prime?"""

    nonprime = lambda a: a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1))
    cnt = len([n for n in range(108100, 125101, 17) if nonprime(n)])
    print("2017 day 23 part 2: %d" % cnt)
