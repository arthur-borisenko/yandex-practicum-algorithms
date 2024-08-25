import array
from typing import Sequence, Iterable


def count_sort_to_orig_arr_iterator(cnt_arr, shift=0):
    """CPU - O(n)
    RAM - O(1)
    May not be used outside count sort
    :param cnt_arr: counts array
    :param shift: value shift of orig array
    :return: result iterator"""
    for i, cnt in enumerate(cnt_arr):
        for _ in range(cnt):
            yield i + shift


def count_sort(seq: Sequence[int]) -> Iterable[int]:
    """CPU - O(n+max(arr))
    RAM - O(max(arr) - min(arr))
    sorts input sequence of positive integers using "count sort"
    :param seq: array to be sorted
    :return: iterator of sorted array"""
    shift = min(seq)
    counts = array.array("q", [0] * (max(seq) - shift + 1))
    for el in seq:
        counts[el - shift] += 1
    return count_sort_to_orig_arr_iterator(counts, shift)


def solve(homes, money):
    """CPU - O(n+max(arr)-min(arr))
    RAM - O(max(arr) - min(arr))"""
    res = 0
    current_money = money
    sorted_homes = count_sort(homes)
    for home in sorted_homes:
        if current_money >= home:
            current_money -= home
            res += 1
    return res


def main():
    """CPU - O(n+max(arr)-min(arr))
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n, money = map(int, inp.readline().split())
        homes = list(map(int, inp.readline().strip().split()))
        print(solve(homes, money), file=outp)


if __name__ == "__main__":
    main()
