def count_increases(nums):
    return sum(1 if nums[i] > nums[i-1] else 0 for i in range(1, len(nums)))

def count_triples(nums):
    return sum(1 if nums[i+2] > nums[i-1] else 0 for i in range(1, len(nums)-2))

with open("day01.txt", "r") as fh:
    nums = [int(line) for line in fh.readlines()]
    print("2021 day 01 part 1: %d" % count_increases(nums))
    print("2021 day 01 part 2: %d" % count_triples(nums))
