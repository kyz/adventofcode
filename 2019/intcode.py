from collections import defaultdict

def computer(program, name=None):
    mem = defaultdict(int)

    # copy program into memory
    for i in range(len(program)):
        mem[i] = program[i]

    ilen = [None, 4, 4, 2, 2, 3, 3, 4, 4, 2]
    amode = [
        lambda o: mem[o],     # position mode
        lambda o: o,          # immediate mode
        lambda o: mem[o] + rb # relative mode
    ]
    pc, rb = 0, 0
    while mem[pc] != 99:
        if name: print("%s pc=%-4d %s" % (name, pc, decode(mem, pc, rb)))
        op = mem[pc] % 100
        x = amode[(mem[pc] // 100) % 10](pc + 1)
        y = amode[(mem[pc] // 1000) % 10](pc + 2)
        z = amode[(mem[pc] // 10000) % 10](pc + 3)
        if   op == 1: mem[z] = mem[x] + mem[y]
        elif op == 2: mem[z] = mem[x] * mem[y]
        elif op == 3: mem[x] = yield
        elif op == 4: yield mem[x]
        elif op == 5: pc = mem[y] - 3 if mem[x] != 0 else pc
        elif op == 6: pc = mem[y] - 3 if mem[x] == 0 else pc
        elif op == 7: mem[z] = 1 if mem[x] < mem[y] else 0
        elif op == 8: mem[z] = 1 if mem[x] == mem[y] else 0
        elif op == 9: rb += mem[x]
        pc += ilen[op]

def decode(mem, pc, rb):
    amode = [
        lambda o: ("mem[%d]"    % o).ljust(11),
        lambda o: ("#%d"        % o).ljust(11),
        lambda o: ("mem[rb+%d]" % o).ljust(11)
    ]
    op = mem[pc] % 100
    x = amode[(mem[pc] // 100) % 10](mem[pc + 1])
    y = amode[(mem[pc] // 1000) % 10](mem[pc + 2])
    z = amode[(mem[pc] // 10000) % 10](mem[pc + 3])
    if   op == 1: return "ADD %s %s %s" % (x, y, z)
    elif op == 2: return "MUL %s %s %s" % (x, y, z)
    elif op == 3: return "IN  %s" % x
    elif op == 4: return "OUT %s" % x
    elif op == 5: return "JNZ %s %s" % (x, y)
    elif op == 6: return "JZ  %s %s" % (x, y)
    elif op == 7: return "SLT %s %s %s" % (x, y, z)
    elif op == 8: return "SEQ %s %s %s" % (x, y, z)
    elif op == 9: return "IRB %s (rb now %d)" % (x, rb + mem[x])
