import array
from typing import Sequence, Iterable


def count_sort_to_orig_arr_iterator(cnt_arr, shift=0, reverse=False) -> Iterable:
    """CPU - O(1) to init, O(1) per iteration
    RAM - O(1)
    Must not be used outside count sort
    """
    _range = range(len(cnt_arr)) if not reverse else reversed(range(len(cnt_arr)))
    for i in _range:
        cnt = cnt_arr[i]
        for _ in range(cnt):
            yield i + shift


def count_sort(seq: Sequence[int], reverse=False) -> Iterable[int]:
    """CPU - O(n+max(arr))
    RAM - O(max(arr) - min(arr))
    Doesn't change input data structure
    Input sequence must contain only non-negative integers
    """
    shift = min(seq, default=0)  # , default=0)
    counts = array.array("q", [0] * (max(seq, default=0) - shift + 1))
    for el in seq:
        counts[el - shift] += 1
    return count_sort_to_orig_arr_iterator(counts, shift, reverse)
