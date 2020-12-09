from collections import defaultdict

# from https://www.geeksforgeeks.org/perfect-sum-problem-print-subsets-given-sum/
def all_subsets(arr, total):
    paths = []
    n = len(arr)

    # dp[i,j] is true if total j is possible with nums[0:i]
    dp = defaultdict(bool)
    for i in range(n):
        dp[i,0] = True
    if arr[0] < total:
        dp[0,arr[0]] = True
    for i in range(1, n):
        for j in range(0, total + 1):
            dp[i,j] = (dp[i-1,j] or dp[i-1,j-arr[i]]) if arr[i] <= j else dp[i-1, j]

    def traverse(i, tot, plen):
        if i == 0 and (tot == 0 or dp[0,tot]):
            return paths.append(plen + (1 if tot else 0))
        if dp[i-1,tot]:
            traverse(i-1, tot, plen)
        if tot >= arr[i] and dp[i-1,tot-arr[i]]:
            traverse(i-1, tot-arr[i], plen+1)
    if dp[n-1,total]:
        traverse(n-1, total, 0)

    return paths

with open("day17.txt") as fh:
    nums = sorted([int(line) for line in fh])
    paths = all_subsets(nums, 150)
    print("2015 day 17 part 1: %d" % len(paths))
    print("2015 day 17 part 2: %d" % paths.count(min(paths)))
