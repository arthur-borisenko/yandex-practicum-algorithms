import math, time
from collections import defaultdict


def parse_input(inp):
    mss = []
    n = int(inp.readline())
    for i in range(n):
        mss.append(tuple(map(int, inp.readline().split())))
    m = int(inp.readline())
    bsm = defaultdict(int)
    for i in range(m):
        x, y = map(int, inp.readline().split())
        bsm[(x, y)] += 1
    return mss, bsm


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        ms, bsm = parse_input(inp)

        i = 0
        mi = None
        mr = 0
        for x1, y1 in ms:
            r = 0
            for x in range(x1 - 20, x1 + 21):
                for y in range(y1 - 20, y1 + 21):
                    if math.dist([x, y], [x1, y1]) <= 20:
                        r += bsm[(x, y)]
            if r > mr:
                mr = r
                mi = i
            i += 1
        print(mi + 1, file=out)


if __name__ == "__main__":
    main()
