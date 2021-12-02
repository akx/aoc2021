lines = [l.strip().split(None, 1) for l in open("../inputs/d02.txt")]
inss = [(ins, int(val)) for (ins, val) in lines]

x = aim = y = 0

for ins, val in inss:
    if ins[0] == "f":
        x += val
        y += val * aim
    elif ins[0] == "u":
        aim -= val
    elif ins[0] == "d":
        aim += val
print(x, y, x * y)
