from io import TextIOWrapper
from typing import Iterable


def pair_sums(l: Iterable[int]) -> dict[int, tuple[int, int]]:
    """CPU - O(k^2)
    RAM - O(k^2)
    where k = len(l)"""
    res = {}
    for i1, el1 in enumerate(l):
        for i2, el2 in enumerate(l):
            if i1 == i2:
                continue
            if el1 + el2 not in res:
                res[el1 + el2] = []
            res[el1 + el2].append((i1, i2))
    return res


def sum_4(a: int, x: list[int]) -> list[tuple[int, int, int, int]]:
    """CPU - O(k^2)
    RAM - O(k^2)
    where k = len(x)"""
    k = len(x)
    quartets = set()
    sums = pair_sums(x)
    for i in range(k):
        for j in range(i + 1, k):
            target = a - x[i] - x[j]
            if target in sums:
                target_indexes = sums[target]
                for target_i1, target_i2 in target_indexes:
                    if (
                        target_i1 == i
                        or target_i2 == i
                        or target_i1 == j
                        or target_i2 == j
                    ):
                        continue
                    quartets.add(
                        tuple(sorted((x[target_i1], x[target_i2], x[i], x[j])))
                    )
    return sorted(quartets)


def parse_input(inp: TextIOWrapper):
    n = int(inp.readline())
    a = int(inp.readline())
    l = list(map(int, inp.readline().split()))
    return n, a, l


def main():
    """CPU - O(n^2)
    RAM - O(n^2)"""
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n, a, x = parse_input(inp)
        res = sum_4(a, x)
        print(len(res), file=out)
        for s in res:
            print(*s, file=out)


if __name__ == "__main__":
    main()
