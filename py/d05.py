import collections
import dataclasses
from typing import Tuple, Iterable


def parse_tup(tup: str) -> Tuple[int, int]:
    return tuple(map(int, tup.split(",", 1)))


@dataclasses.dataclass
class Seg:
    x0: int
    y0: int
    x1: int
    y1: int

    @classmethod
    def from_str(cls, s: str) -> 'Seg':
        a, _, b = s.strip().partition(" -> ")
        x0, y0 = parse_tup(a)
        x1, y1 = parse_tup(b)
        x0, x1 = sorted((x0, x1))
        y0, y1 = sorted((y0, y1))
        seg = Seg(x0=x0, y0=y0, x1=x1, y1=y1)
        return seg

    @property
    def is_horz_or_vert(self) -> bool:
        return self.x0 == self.x1 or self.y0 == self.y1

    def iter_points(self) -> Iterable[Tuple[int, int]]:
        if self.x0 == self.x1:  # vert
            yield from ((self.x0, y) for y in range(self.y0, self.y1 + 1))
            return
        if self.y0 == self.y1:  # horz
            yield from ((x, self.y0) for x in range(self.x0, self.x1 + 1))
            return
        raise NotImplementedError("Ni!")


def parse_input(fn):
    with open(fn) as f:
        for line in f:
            yield Seg.from_str(line)


def main():
    cnt = collections.Counter()
    for seg in parse_input("../inputs/d05.txt"):
        if not seg.is_horz_or_vert:
            continue
        for pt in seg.iter_points():
            cnt[pt] += 1
    for y in range(10):
        line = "".join(f"{(cnt[x, y] or '.'):1}" for x in range(10))
        print(line)
    overlaps = len([pt for (pt, n) in cnt.items() if n > 1])
    print(overlaps)



if __name__ == '__main__':
    main()
