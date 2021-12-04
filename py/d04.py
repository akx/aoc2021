from typing import List, Tuple


def read_data(fn):
    numbers = None
    grids = []
    curr_grid = None
    for line in open(fn):
        line = line.strip()
        if not line:
            curr_grid = None
            continue
        if not numbers:
            numbers = [int(x) for x in line.split(",")]
            continue
        if not curr_grid:
            curr_grid = []
            grids.append(curr_grid)
        curr_grid.append([int(x) for x in line.split()])
    return (numbers, grids)


def check_win(grid: List[List[int]], drawn_numbers: List[int]) -> Tuple[bool, int]:
    mgrid = [[None if n in drawn_numbers else n for n in row] for row in grid]
    if any(c.count(None) == 5 for c in mgrid) or any(
        c.count(None) == 5 for c in zip(*mgrid)
    ):
        return (True, sum(sum(num for num in col if num is not None) for col in mgrid))
    return (False, 0)


def main():
    numbers, grids = read_data("../inputs/d04.txt")
    for n in range(len(numbers)):
        drawn_numbers = numbers[:n]
        for i, grid in enumerate(grids):
            win, checksum = check_win(grid, drawn_numbers)
            if win:
                print(i, win, checksum * drawn_numbers[-1])
                return


if __name__ == "__main__":
    main()
