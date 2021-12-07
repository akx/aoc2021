import collections
from typing import Dict, List

with open("../inputs/d06.txt") as f:
    data = [int(x) for x in f.read().strip().split(",")]

# data = [3, 4, 3, 1, 2]


def iterate(fish_timers: List[int]) -> List[int]:
    new_count = fish_timers[0]
    new_timers = fish_timers[1:] + [new_count]
    new_timers[6] += new_count
    return new_timers


fish_time_counts = dict(collections.Counter(data))
fish_timers = [fish_time_counts.get(x, 0) for x in range(9)]

for x in range(1, 257):
    fish_timers = iterate(fish_timers)
    print("after day", x, ":", sum(fish_timers))
