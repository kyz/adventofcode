import functools, itertools

OP, CL = "[", "]"

def parse_snailnum(num):
    valid_chars = set("[]0123456789")
    return [n if n in {OP, CL} else int(n) for n in num if n in valid_chars]

def isint(n):
    return isinstance(n, int)

def find_explodable(num):
    depth = 0
    for i in range(len(num)-3):
        if num[i] == OP: depth += 1
        if num[i] == CL: depth -= 1
        if depth > 4 and num[i] == OP and isint(num[i+1]) and isint(num[i+2]) and num[i+3] == CL:
            return i
    return None

def find_splittable(num):
    for i in range(len(num)):
        if isint(num[i]) and num[i] >= 10:
            return i
    return None

def snailreduce(num):
    while True:
        e = find_explodable(num)
        if e:
            # add left number in pair to first number left of the pair
            for i in range(e-1, -1, -1):
                if isint(num[i]):
                    num[i] += num[e+1]
                    break
            # add right number in pair to first number right of the pair
            for i in range(e+4, len(num)):
                if isint(num[i]):
                    num[i] += num[e+2]
                    break
            # replace the pair with literal zero
            num = num[:e] + [0] + num[e+4:]
            continue

        s = find_splittable(num)
        if s:
            num = num[:s] + [OP, num[s] // 2, num[s] - (num[s] // 2), CL] + num[s+1:]
            continue

        # neither an explode or split happened, so reduction is done
        return num

def snailsum(nums):
    return functools.reduce(lambda a, b: snailreduce([OP] + a + b + [CL]), nums)

def magnitude(num):
    while len(num) > 1:
        for i in range(len(num)-3):
            if num[i] == OP and isint(num[i+1]) and isint(num[i+2]) and num[i+3] == CL:
                num = num[:i] + [num[i+1] * 3 + num[i+2] * 2] + num[i+4:]
                break
    return num[0]

def max_magnitude(nums):
    return max(magnitude(snailsum([a,b])) for a, b in itertools.permutations(nums, 2))

with open("day18.txt", "r") as fh:
    numbers = [parse_snailnum(line) for line in fh]
    print("2021 day 18 part 1: %d" % magnitude(snailsum(numbers)))
    print("2021 day 18 part 2: %d" % max_magnitude(numbers))
