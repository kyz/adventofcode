def follow(data):
    letters, steps = [], 0
    x, y, d = 0, 0, (0,1)

    # find start
    while data[y][x] == " ":
        x += 1

    while True:
        c = data[y][x]
        if c == "+":
            d = [nd for nd in [(0,-1), (0,1), (-1,0), (1,0)]
                 if nd != (-d[0], -d[1])
                 and data[y + nd[1]][x + nd[0]] != " "][0]
        elif c.isalpha():
            letters.append(c)
        elif c == " ":
            return letters, steps
        x += d[0]
        y += d[1]
        steps += 1

with open("day19.txt") as f:
    data = [line for line in f]
    letters, steps = follow(data)
    print("2017 day 19 part 1: %s" % "".join(letters))
    print("2017 day 19 part 2: %d" % steps)
