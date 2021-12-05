import collections
import dataclasses
from typing import Tuple, Iterable


def parse_tup(tup: str) -> Tuple[int, int]:
    return tuple(map(int, tup.split(",", 1)))


def cmp_0(a, b):
    if a < b:
        return -1
    if a > b:
        return +1
    return 0


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
        seg = Seg(x0=x0, y0=y0, x1=x1, y1=y1)
        return seg

    @property
    def is_horz_or_vert(self) -> bool:
        return self.x0 == self.x1 or self.y0 == self.y1

    def iter_points(self) -> Iterable[Tuple[int, int]]:
        dx = cmp_0(self.x1, self.x0)
        dy = cmp_0(self.y1, self.y0)
        x, y = self.x0, self.y0
        assert (dx, dy) != (0, 0), self
        print((x, y), "delta=", (dx, dy))
        while True:
            yield (x, y)
            x += dx
            y += dy
            if (x, y) == (self.x1, self.y1):
                yield (x, y)
                return


def parse_input(fn):
    with open(fn) as f:
        for line in f:
            yield Seg.from_str(line)


def main():
    cnt = collections.Counter()
    for seg in parse_input("../inputs/d05.txt"):
        for pt in seg.iter_points():
            cnt[pt] += 1
    for y in range(10):
        line = "".join(f"{(cnt[x, y] or '.'):1}" for x in range(10))
        print(line)
    overlaps = len([pt for (pt, n) in cnt.items() if n > 1])
    print(overlaps)


if __name__ == '__main__':
    main()
