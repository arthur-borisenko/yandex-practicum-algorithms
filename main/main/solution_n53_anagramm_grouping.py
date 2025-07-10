from typing import Iterable


def solve(l: Iterable[str]) -> Iterable[Iterable[int]]:
    """CPU - O(s log(s) + n*s)
    RAM - O(n + s)
    where n - input data length; s - count of unique symbols in input data"""
    groups = {}
    symbols = []
    symbols_seen = set()
    for el in l:
        for symbol in el:
            if symbol not in symbols_seen:
                symbols_seen.add(symbol)
                symbols.append(symbol)
    symbols.sort()
    for i, el in enumerate(l):
        counts: dict = {}
        s_sorted = []
        for symbol in el:
            counts[symbol] = counts.get(symbol, 0) + 1
        for symbol in symbols:
            s_sorted.append(counts.get(symbol, 0) * symbol)
        groups["".join(s_sorted)] = groups.get("".join(s_sorted), [])
        groups["".join(s_sorted)].append(i)
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
