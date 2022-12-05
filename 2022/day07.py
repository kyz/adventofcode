def parse_cmds(cmds):
    fs, cwd, ptr = {}, None, None
    for c in cmds:
        if c[0] == '$' and c[1] == 'cd':
            if c[2] == '/':    cwd = []
            elif c[2] == '..': cwd.pop()
            else:              cwd.append(c[2])
            # move ptr to the appropriate place in fs
            ptr = fs
            for c in cwd: ptr = ptr[c]
        elif c[0] != '$' and c[1] not in ptr: # assume dir listing
            ptr[c[1]] = {} if c[0] == 'dir' else int(c[0])
    return fs

dir_sizes = []
def walk(fs):
    size = sum(walk(e) if type(e) == dict else e for e in fs.values())
    dir_sizes.append(size)
    return size

with open("day07.txt", "r") as fh:
    fs = parse_cmds([line.split() for line in fh])
    walk(fs)
    print("2022 day 07 part 1: %d" % sum(d for d in dir_sizes if d <= 100000))
    print("2022 day 07 part 2: %d" % min(d for d in dir_sizes if dir_sizes[-1] - d <= 40000000))
