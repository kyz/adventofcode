def find_invalid(nums, n):
    for i in range(n, len(nums)):
        sums = {nums[i-n+j] + nums[i-n+k] for j in range(n) for k in range(n) if j != k}
        if nums[i] not in sums:
            return nums[i]

def find_sum(nums, target):
    for i in range(len(nums)):
        j, total = i, 0
        while j < len(nums) and total < target:
            total += nums[j]
            j += 1
        if total == target:
            return min(nums[i:j+1]) + max(nums[i:j+1])

with open("day09.txt", "r") as fh:
    nums = [int(x) for x in fh.readlines()]
    inv = find_invalid(nums, 25)
    print("2020 day 09 part 1: %d" % inv)
    print("2020 day 09 part 2: %d" % find_sum(nums, inv))

