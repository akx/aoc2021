import collections

lines = [l.strip() for l in open("../inputs/d03.txt")]


def find(look_idx):
    candidates = set(lines)
    for bit_idx in range(len(lines[0])):
        counter = collections.Counter(
            [cand[bit_idx] for cand in candidates]
        ).most_common()
        assert len(counter) == 2
        eqc = counter[0][1] == counter[1][1]
        print(bit_idx, eqc, candidates)
        if eqc:
            flag = str(1 - look_idx)
        else:
            flag = counter[look_idx][0]
        print(f"keeping candidates with bit {bit_idx} == {flag}")
        candidates = {c for c in candidates if c[bit_idx] == flag}
        if len(candidates) == 1:
            cbin = next(iter(candidates))
            print("->", cbin, int(cbin, 2))
            return int(cbin, 2)


f0 = find(0)
f1 = find(1)
print(f0, f1, f0 * f1)
