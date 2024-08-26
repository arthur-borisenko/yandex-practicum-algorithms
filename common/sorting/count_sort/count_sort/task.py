import array
from typing import Sequence, Iterable


def count_sort(seq: Sequence[int], reverse=False) -> Iterable[int]:
    """CPU - O(n+max(arr))
    RAM - O(max(arr) - min(arr))
    Doesn't change input data structure
    Input sequence must contain only non-negative integers
    """
    shift = min(seq, default=0)
    counts = array.array("q", [0] * (max(seq, default=0) - shift + 1))
    for el in seq:
        counts[el - shift] += 1
    _range = range(len(counts)) if not reverse else reversed(range(len(counts)))
    for i in _range:
        cnt = counts[i]
        for _ in range(cnt):
            yield i + shift
