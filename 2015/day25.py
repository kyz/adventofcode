def codegen(row, col):
    code = 20151125
    for i in range((((row + col - 2) * (row + col - 1)) // 2) + col - 1):
        code = (code * 252533) % 33554393
    return code

print("2015 day 25 part 1: %d" % codegen(2978, 3083))
