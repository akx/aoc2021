import collections

lines = [l.strip() for l in open("../inputs/d03.txt")]

z = [collections.Counter(l).most_common() for l in zip(*lines)]

zcommon = int("".join([c[0][0] for c in z]), 2)
zrare = int("".join([c[1][0] for c in z]), 2)

print(zcommon, zrare, zcommon * zrare)
