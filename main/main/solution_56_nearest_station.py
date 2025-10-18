import math
from io import TextIOWrapper


def get_distance(pos1: tuple[int, int], pos2: tuple[int, int]) -> float:
    pos1_x, pos1_y = pos1
    pos2_x, pos2_y = pos2
    return math.sqrt((pos1_x - pos2_x) ** 2 + (pos1_y - pos2_y) ** 2)


def parse_input(inp: TextIOWrapper):
    mstations = []
    bstations = []
    n = int(inp.readline())
    for i in range(n):
        mstations.append((tuple(map(int, inp.readline().split())), i))
    m = int(inp.readline())
    for i in range(m):
        bstations.append(tuple(map(int, inp.readline().split())))
    return mstations, bstations


def solve(
    mstations: list[tuple[tuple[int, int], int]], bstations: list[tuple[int, int]]
):
    ans = (None, 0)
    for mstation in mstations:
        x = 0
        for bstation in bstations:
            if get_distance((mstation[0]), bstation) < 20:
                x += 1
        if x > ans[1]:
            ans = (mstation, x)
    return ans[0]


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as out:
        mstations, bstations = parse_input(inp)
        ans = solve(mstations, bstations)
        print(ans, file=out)


if __name__ == "__main__":
    main()
