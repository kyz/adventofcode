import math

def divisors(n):
    return (i for i in range(1, int(math.sqrt(n)) + 1) if (n % i) == 0)

# presents for house n = 10 * sum(positive factors of n)
def p1(n):
    return 10 * sum(((i if i == n//i else i + n//i) for i in divisors(n)))

# presents for house n = 11 * sum(positive factors of n where n/factor <= 50)
def p2(n):
    return 11 * sum(( (i    if n//i <= 50 else 0) +
                      (n//i if i    <= 50 and n//i != i else 0) for i in divisors(n)))

def search(f, n, l, h, step=1):
    for i in range(l, h+1, step):
        if f(i) >= n: return l, i
    return l, h

# to narrow the search space:
# - the slope of p1(x)/x is between 10 and ~45
# - the slope of p2(x)/x is between 11 and ~43
# - checking every 5th value eliminates ~250,000 candidates with ~8,000 tests

def search1(n):
    lo, hi = search(p1, n, n // 45, n // 10, 5)
    return search(p1, n, lo, hi)[1]

def search2(n):
    lo, hi = search(p2, n, n // 43, n // 11, 5)
    return search(p2, n, lo, hi)[1]

presents_target = 33100000
print("2015 day 20 part 1: %d" % search1(presents_target))
print("2015 day 20 part 2: %d" % search2(presents_target))
