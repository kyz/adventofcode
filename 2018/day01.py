def dup_freq(nums):
    seen = set()
    freq = 0
    while True:
        for n in nums:
            freq += n
            if freq in seen: return freq # exit condition
            seen.add(freq)

with open("day01.txt", "r") as fh:
    nums = [int(line) for line in fh]
    print("2018 day 01 part 1: %d" % sum(nums))
    print("2018 day 01 part 2: %d" % dup_freq(nums))
