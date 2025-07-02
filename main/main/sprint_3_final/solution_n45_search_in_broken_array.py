from typing import Sequence


def search_ordered_circular_array_start(
    sequence: Sequence, left: int = None, right: int = None
) -> int:
    """Finds last element in left sorted part of the semi-sorted number array with unique items with one or no disorder.
    If there is no disorder, returns -1.
    CPU - O(log n)
    RAM - O(1)"""
    if left is None:
        left = 0
    if right is None:
        right = len(sequence) - 1
    while left < right:
        if sequence[left] <= sequence[right]:
            return -1
        mid = left + (right - left) // 2
        if mid + 1 < len(sequence) and sequence[mid] > sequence[mid + 1]:
            return mid
        if sequence[mid] > sequence[right]:
            left = mid + 1
        else:
            right = mid
    return -1


class CircularArray(Sequence):
    def __init__(self, arr, end_i):
        self.arr = arr
        self.shift = -(len(arr) - end_i - 1)

    def to_internal_array_index(self, i):
        return (i + self.shift) % len(self.arr)

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, i):
        return self.arr[self.to_internal_array_index(i)]

    def __setitem__(self, i, val):
        self.arr[self.to_internal_array_index(i)] = val

    def __iter__(self):
        class _Iterator:
            def __init__(self, seq):
                self.i = -1
                self.arr = seq

            def __iter__(self):
                return self

            def __next__(self):
                self.i += 1
                if self.i < len(self.arr):
                    return self.arr[self.i]
                raise StopIteration

        return _Iterator(self)


def search(sequence: Sequence, target) -> int:
    """Classic binary search implementation.
    CPU - O(log n)
    RAM - O(1)"""
    left = 0
    right = len(sequence) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if sequence[mid] == target:
            return mid
        elif sequence[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def broken_search(nums, target) -> int:
    """Finds element target_index in the semi-sorted number array with unique with one or no disorder.
    If there is no such element, returns -1.
    CPU - O(log n)
    RAM - O(1)"""
    broken_index = search_ordered_circular_array_start(nums)
    if broken_index != -1:
        ring_array = CircularArray(nums, broken_index)
        target_broken_index = search(ring_array, target)
        if target_broken_index == -1:
            return -1
        target_index = ring_array.to_internal_array_index(target_broken_index)
        return target_index
    else:
        target_broken_index = search(nums, target)
        if target_broken_index == -1:
            return -1
        return target_broken_index


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
