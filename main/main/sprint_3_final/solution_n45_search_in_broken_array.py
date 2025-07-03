from typing import Sequence, Any


def search_sorted_circular_array_start(
    sequence: Sequence, left: int = 0, right: int = None
) -> int:
    """Finds the end of a sorted ring array with unique items.
    CPU - O(log n)
    RAM - O(1)"""
    if right is None:
        right = len(sequence) - 1
    if sequence[left] <= sequence[right]:
        return -1

    while left < right:
        mid = left + (right - left) // 2
        if sequence[mid] > sequence[mid + 1]:
            return mid
        if sequence[mid] > sequence[right]:
            left = mid + 1
        else:
            right = mid
    return left


class CircularArray(Sequence):
    def __init__(self, arr, pivot_index):
        self.arr = arr
        self.pivot = pivot_index + 1

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, i):
        return self.arr[self.to_original_index(i)]

    def to_original_index(self, i):
        return (i + self.pivot) % len(self.arr)


def search(sequence: Sequence, target: Any) -> int:
    """Classic binary search implementation.
    CPU - O(log n)
    RAM - O(1)"""
    left, right = 0, len(sequence) - 1
    while left <= right:
        mid = (left + right) // 2
        if sequence[mid] == target:
            return mid
        elif sequence[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def broken_search(nums, target) -> int:
    """Finds element in the semi-sorted array with unique elements and one or no disorder.
    Returns -1 if element is not found.
    CPU - O(log n)
    RAM - O(1)"""
    broken_index = search_sorted_circular_array_start(nums)
    if broken_index != -1:
        ring_array = CircularArray(nums, broken_index)
        idx = search(ring_array, target)
        return ring_array.to_original_index(idx) if idx != -1 else -1
    else:
        return search(nums, target)


def test():
    # Обычный случай с разрывом
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6

    # Поиск в отсортированном массиве без разрыва
    arr = [1, 2, 3, 4, 5]
    assert broken_search(arr, 3) == 2

    # Элемент не найден
    assert broken_search(arr, 6) == -1

    # Массив с разрывом, поиск элемента до разрыва
    arr = [10, 20, 30, 1, 2, 3]
    assert broken_search(arr, 20) == 1
