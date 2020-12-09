def find_pair(nums):
    for a in nums:
        for b in nums:
            if (a + b) == 2020:
                return a * b

def find_triple(nums):
    for a in nums:
        for b in nums:
            for c in nums:
                if (a + b + c) == 2020:
                    return a * b * c

with open("day01.txt", "r") as fh:
    nums = [int(line) for line in fh.readlines()]
    print("2020 day 01 part 1: %d" % find_pair(nums))
    print("2020 day 01 part 2: %d" % find_triple(nums))
