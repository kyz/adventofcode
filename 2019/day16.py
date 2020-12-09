def fft(nums):
    l = len(nums)
    for phase in range(100):
        nums = [abs(
            sum([sum(nums[j:j+(i+1)]) for j in range(i,     l, (i+1)*4)]) -
            sum([sum(nums[j:j+(i+1)]) for j in range(i*3+2, l, (i+1)*4)])
        ) % 10 for i in range(l)]
    return nums

def fft2(nums, skip):
    nums = (nums * 10000)[skip:]
    for phase in range(100):
        for i in range(len(nums) - 2, -1, -1):
            nums[i] = (nums[i] + nums[i+1]) % 10
    return nums

def checksum(nums):
    return "".join(map(str, nums[:8]))

with open("day16.txt") as fh:
    data = fh.readline().strip()
    nums = [int(d) for d in data]
    skip = int(data[0:7])
    print("2019 day 16 part 1: %s" % checksum(fft(nums)))
    print("2019 day 16 part 2: %s" % checksum(fft2(nums, skip)))
