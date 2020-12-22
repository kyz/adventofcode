# greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# lowest common multiple
def lcm(a, b):
    return (a * b) // gcd(a, b)
