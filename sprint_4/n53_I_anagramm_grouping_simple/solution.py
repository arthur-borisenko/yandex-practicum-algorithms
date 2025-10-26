from typing import Iterable


def solve(l: Iterable[str]) -> Iterable[Iterable[int]]:
    """CPU - O(sum(x log x)
    RAM - O(n)
    where n - input data length, x - each element length"""
    groups = {}
    for i, el in enumerate(l):
        s_sorted = "".join(sorted(el))
        groups[s_sorted] = groups.get(s_sorted, [])
        groups[s_sorted].append(i)
    return sorted(groups.values())


def main():
    """CPU - O(s log(s) + n*s)
    RAM - O(n + s)
    where n - input data length; s - count of unique symbols in input data"""
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        l = inp.readline().split()
        for group in solve(l):
            print(*group, file=out)


if __name__ == "__main__":
    main()
