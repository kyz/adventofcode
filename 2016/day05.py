import hashlib

door_id = "abbhdwsy"

known_answer = [
    1739529, 1910966, 1997199, 2854555, 2963716, 3237361, 4063427, 7777889, 8460345,
    9417946, 12389322, 12434824, 12850790, 12942170, 12991290, 13256331,  14024976,
    15299586, 17786793, 17931630, 19357601, 19359925, 19808330, 20214395, 22339420,
    23135423, 24055333, 24538150, 25056365, 25651067
]

part1 = []
part2 = {}
#for i in range(99999999):
for i in known_answer:
    h = hashlib.md5((door_id + str(i)).encode("ASCII")).hexdigest()
    if h[:5] == "00000":
        part1.append(h[5])
        if h[5] not in part2 and "0" <= h[5] <= "7":
            part2[h[5]] = h[6]

        if len(part1) == 8:
            print("2016 day 05 part 1: " + "".join(part1))

        if len(part2) == 8:
            print("2016 day 05 part 2: " + "".join(part2[k] for k in sorted(part2)))
            break

