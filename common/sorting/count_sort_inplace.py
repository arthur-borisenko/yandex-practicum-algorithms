import array
from typing import MutableSequence


def count_sort(arr: MutableSequence[int], reverse=False) -> None:
    """CPU - O(n+max(arr))
    RAM - O(max(arr))
    Input sequence must contain only non-negative integers
    """
    counts = array.array("q", [0] * (max(arr, default=0) + 1))
    for val in arr:
        counts[val] = counts[val] + 1
    index = 0
    for i, cnt in enumerate(counts):
        for _ in range(cnt):
            arr[index if not reverse else -(index + 1)] = i
            index += 1
