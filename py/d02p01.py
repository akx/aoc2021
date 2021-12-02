lines = [l.strip().split(None, 1) for l in open("../inputs/d02.txt")]
inss = [(ins, int(val)) for (ins, val) in lines]

x = y = 0

for ins, val in inss:
    if ins[0] == "f":
        x += val
    elif ins[0] == "u":
        y -= val
    elif ins[0] == "d":
        y += val
print(x, y, x * y)
