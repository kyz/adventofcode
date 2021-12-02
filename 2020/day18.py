def order1(o, n):
    return o != "("

def order2(o, n):
    p = {"+": 3, "*": 2, "(": 1, ")": 1}
    return p[o] > p[n]

# https://en.wikipedia.org/wiki/Shunting-yard_algorithm
def evaluate(expr, eval_needed):
    ts, vs = [], []
    for t in ("(%s)" % expr): # wrap expr in parens
        if "0" <= t <= "9":
            vs.append(int(t))
        elif t == "(":
            ts.append(t)
        elif t in {")", "*", "+"}:
            while eval_needed(ts[-1], t):
                op, v1, v2 = ts.pop(), vs.pop(), vs.pop()
                vs.append(v1 + v2 if op == "+" else v1 * v2)
            if t == ")":
                ts.pop() # remove matching paren
            else:
                ts.append(t)
    return vs.pop()

with open("day18.txt", "r") as fh:
    exprs = fh.readlines()
    print("2020 day 18 part 1: %d" % sum(evaluate(expr, order1) for expr in exprs))
    print("2020 day 18 part 2: %d" % sum(evaluate(expr, order2) for expr in exprs))
