with open("../inputs/d06.txt") as f:
    data = [int(x) for x in f.read().strip().split(",")]

# data = [3, 4, 3, 1, 2]


def iterate(data):
    new = [6 if x == 0 else x - 1 for x in data]
    return new + [8] * data.count(0)


print("initial....", ":", len(data), "".join(str(x) for x in data))

for x in range(1, 81):
    data = iterate(data)
    print("after day", x, ":", len(data))  # , "".join(str(x) for x in data))
