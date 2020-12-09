from hashlib import md5

prefix = b"ckczppom"
for i in range(400000):
    if md5(prefix + str(i).encode("ascii")).hexdigest()[:5] == "00000":
        print("2015 day 4 part 1: %d" % i)
        break
for i in range(3900000, 4000000): # start from 3900000 now we know answer
    if md5(prefix + str(i).encode("ascii")).hexdigest()[:6] == "000000":
        print("2015 day 4 part 2: %d" % i)
        break
