from collections import Counter

def popcnt(nums):
    return [Counter(i).most_common(2) for i in zip(*nums)]

def power_consumption(nums):
    gamma   = int("".join(p[0][0] for p in popcnt(nums)), 2)
    epsilon = int("".join(p[1][0] for p in popcnt(nums)), 2)
    return gamma * epsilon

def filter_nums(nums, rank, tiebreak):
    for i in range(len(nums[0])):
        p = popcnt(nums)[i]
        equally_common = p[0][1] == p[1][1]
        bit = tiebreak if equally_common else p[rank][0]
        nums = [n for n in nums if n[i] == bit]
        if len(nums) == 1:
            return nums[0]

def life_support_rating(nums):
    oxy = filter_nums(nums, 0, '1')
    co2 = filter_nums(nums, 1, '0')
    return int(oxy, 2) * int(co2, 2)

with open("day03.txt", "r") as fh:
    nums = [line.strip() for line in fh.readlines()]
    print("2021 day 03 part 1: %d" % power_consumption(nums))
    print("2021 day 03 part 2: %d" % life_support_rating(nums))
