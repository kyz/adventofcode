numbers = [9,3,1,0,8,4]

def say_numbers(max_turn):
    ls = [0] * max_turn
    for turn, n in enumerate(numbers):
        ls[n] = turn + 1
    last = numbers[-1]
    for turn in range(len(numbers), max_turn):
        n = turn - ls[last] if ls[last] else 0
        ls[last] = turn
        last = n
    return last

print("2020 day 15 part 1: %d" % say_numbers(2020))
print("2020 day 15 part 1: %d" % say_numbers(30000000))

