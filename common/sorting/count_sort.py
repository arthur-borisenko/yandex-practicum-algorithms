import array
from typing import MutableSequence, Sequence, Iterable


# count sort with input sequence change
def count_sort(arr: MutableSequence[int], reverse=False) -> None:
    """CPU - O(n+max(arr))
    RAM - O(max(arr))
    sort input array of ints (non-negative) with "count sort"
    """
    counts = array.array("q", [0] * (max(arr, default=0) + 1))
    for val in arr:
        counts[val] = counts[val] + 1
    index = 0
    for i, cnt in enumerate(counts):
        for _ in range(cnt):
            arr[index if not reverse else -(index + 1)] = i
            index += 1


# count sort creating new iterator
def count_sort_to_orig_arr_iterator(cnt_arr, shift=0, reverse=False):
    """CPU - O(n)
    RAM - O(1)
    May not be used outside count sort
    :param cnt_arr: counts array
    :param shift: value shift of orig array
    :param reverse: reverse order of result
    :return: iterator"""
    _range = range(len(cnt_arr)) if not reverse else reversed(range(len(cnt_arr)))
    for i in _range:
        cnt = cnt_arr[i]
        for _ in range(cnt):
            yield i + shift


def count_sorted(seq: Sequence[int], reverse=False) -> Iterable[int]:
    """CPU - O(n+max(arr))
    RAM - O(max(arr) - min(arr))
    sorts input sequence of positive integers using "count sort"
    :param seq: array to be sorted
    :return: iterator of sorted array"""
    shift = min(seq, default=0)  # , default=0)
    counts = array.array("q", [0] * (max(seq, default=0) - shift + 1))
    for el in seq:
        counts[el - shift] += 1
    return count_sort_to_orig_arr_iterator(counts, shift, reverse)
