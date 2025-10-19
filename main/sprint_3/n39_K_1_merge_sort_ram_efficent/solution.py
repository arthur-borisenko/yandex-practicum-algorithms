from typing import Sequence


def merge_sort(arr: Sequence, lf: int, rg: int) -> None:
    """
    Sorts arr[lf:rg]. Other parts of arr are not modified
    all arr elements must support comparsion
    CPU - O(n log(n))
    RAM - O(log(n))
    n - interval length rg - lf
    """
    if rg - lf > 1:
        mid = (rg + lf) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        arr[lf:rg] = merge(arr, lf, mid, rg)


def merge(arr, lf, mid, rg):
    left_len = mid - lf
    right_len = rg - mid
    left_i, right_i = lf, mid
    for i in range(left_len + right_len):
        if left_i < mid and (right_i >= rg or arr[left_i] <= arr[right_i]):
            yield arr[left_i]
            left_i += 1
        else:
            yield arr[right_i]
            right_i += 1
