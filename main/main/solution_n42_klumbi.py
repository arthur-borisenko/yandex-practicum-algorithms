import math
from typing import Iterable


def main():
    """CPU - O(n log(n))
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        lns = inp.readlines()
        parsed_lines: Iterable[list[int]] = map(
            lambda l: list(map(int, l.split())), lns
        )
        print_output(merge_overlapping_intervals(parsed_lines), file=outp)


def print_output(out, file):
    for line in out:
        print(*line, file=file)


def merge_overlapping_intervals(lines: Iterable[list[int]]) -> Iterable[list[int]]:
    """CPU - O(n log(n))
    RAM - O(n)"""
    max_end = -math.inf
    max_end_pair = -1
    res = []
    sorted_lns = sorted(lines)
    for index,(start,end) in enumerate(sorted_lns):
        if start > max_end:
            res.append([start, end])
            max_end = end
            max_end_pair = index
        elif end > max_end:
            res[max_end_pair][1] = end
            max_end = end
    return res


if __name__ == "__main__":
    main()
