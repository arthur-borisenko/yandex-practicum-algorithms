import array
from typing import Sequence, Iterable


def count_sort_to_orig_arr_iterator(cnt_arr, shift=0):
    for i, cnt in enumerate(cnt_arr):
        for _ in range(cnt):
            yield i + shift


def count_sort(seq: Sequence[int]) -> Iterable[int]:
    """CPU - O(n + max(arr) - min(arr))
    RAM - O(max(arr) - min(arr))
    sorts input sequence of non-negative integers using "count sort"
    :param seq: array of non-negative integers(including 0) to be sorted
    :return: iterator of sorted array"""
    shift = min(seq)
    counts = array.array("q", [0] * (max(seq) - shift + 1))
    for el in seq:
        counts[el - shift] += 1
    return count_sort_to_orig_arr_iterator(counts, shift)


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        items = list(map(int, inp.readline().strip().split()))
        print(*count_sort(items), file=outp)


if __name__ == "__main__":
    main()
