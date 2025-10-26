from typing import Iterable


def solve(l: Iterable[str]) -> Iterable[Iterable[int]]:
    """CPU - O(s log(s) + n*s)
    RAM - O(n + s)
    where n - input data length; s - count of unique symbols in input data"""
    symbols_set = set()
    for el in l:
        for symbol in el:
            symbols_set.add(symbol)
    symbols = sorted(symbols_set)
    groups = {}
    for i, el in enumerate(l):
        counts: dict = {}
        for symbol in el:
            counts[symbol] = counts.get(symbol, 0) + 1
        s_sorted_list = []
        for symbol in symbols:
            s_sorted_list.append(counts.get(symbol, 0) * symbol)
        s_sorted = "".join(s_sorted_list)
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
