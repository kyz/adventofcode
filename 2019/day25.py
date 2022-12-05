import sys, intcode, re

def readline(cpu):
    line = []
    try:
        out = next(cpu)
        while out is not None:
            line.append(chr(out))
            out = next(cpu)
    except StopIteration:
        pass
    return "".join(line)

def send(cpu, command):
    for c in command:
        out = cpu.send(ord(c))
    return chr(out) + readline(cpu)
    
def play(p):
    cpu = intcode.computer(p)
    print(readline(cpu))
    while True:
        print(send(cpu, sys.stdin.readline()))

def autoplay(p):
    cpu = intcode.computer(p)
    readline(cpu)
    commands = [
        "south", "south", "south", "south", "take festive hat",
        "north", "north", "north", "take whirled peas",
        "north", "north", "take coin",
        "north", "north", "west", "south", "west", "take mutex",
        "west", "south", "east"
    ]
    for c in commands:
        out = send(cpu, c + "\n")
    return re.search(r"typing (\d+) on", out).group(1)

    
with open("day25.txt") as fh:
    p = [int(c) for c in fh.readline().split(",")]
    #play(p)
    print("2019 day 25 part 1: %s" % autoplay(p))
