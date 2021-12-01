from collections import deque

meas = [int(l.split(None)[0]) for l in open("../inputs/d01p01.txt")]


def window(x, n=3):
    q = deque(maxlen=n)
    for i in x:
        q.append(i)
        if len(q) == n:
            yield sum(q)


last = None
n = 0
for ent in window(meas, 3):
    if last is None:
        last = ent
    if ent > last:
        n += 1
    last = ent
print(n)
