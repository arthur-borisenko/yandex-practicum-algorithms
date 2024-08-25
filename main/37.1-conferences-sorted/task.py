def _count(arr):
    """CPU - O(n)
    RAM - O(n)"""
    counts = {}
    for el in arr:
        counts[el] = counts.get(el, 0) + 1
    return counts


def slice_generator(iterable, start, stop):
    for _ in range(start):
        next(iterable)
    for _ in range(stop):
        try:
            res = next(iterable)
        except StopIteration:
            break
        else:
            yield res


def main():
    """CPU - O(n log n)
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        arr = map(int, inp.readline().split())
        k = int(inp.readline())
        key = lambda x: (x[1], -x[0])
        counts = _count(arr).items()
        sorted_counts = sorted(counts, key=key, reverse=True)
        res = map(lambda x: str(x[0]), sorted_counts)
        sliced = slice_generator(res, 0, k)
        print(*sliced, file=outp)


if __name__ == "__main__":
    main()
