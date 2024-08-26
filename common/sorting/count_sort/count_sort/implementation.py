import array
from typing import Sequence, Iterable


def count_sort_to_orig_arr_iterator(cnt_arr, shift=0, reverse=False):
    """CPU - O(n)
    RAM - O(1)
    Must not be used outside count sort
    :param cnt_arr: counts array
    :param shift: value shift of orig array
    :param reverse: reverse order of result
    :return: iterator"""
    _range = range(len(cnt_arr)) if not reverse else reversed(range(len(cnt_arr)))
    for i in _range:
        cnt = cnt_arr[i]
        for _ in range(cnt):
            yield i + shift


def count_sort(seq: Sequence[int], reverse=False) -> Iterable[int]:
    """CPU - O(n+max(arr))
    RAM - O(max(arr) - min(arr))
    Don't change input data structure
    sorts input sequence of positive integers using "count sort"
    :param seq: array to be sorted
    :return: iterator of sorted array"""
    shift = min(seq, default=0)  # , default=0)
    counts = array.array("q", [0] * (max(seq, default=0) - shift + 1))
    for el in seq:
        counts[el - shift] += 1
    return count_sort_to_orig_arr_iterator(counts, shift, reverse)
