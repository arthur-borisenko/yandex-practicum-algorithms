from statistics import median
from typing import MutableSequence, Any, Sequence


def find_pivot(array: Sequence, left, right):
    return median((array[left + (right - left) // 2], array[left], array[right]))


def reorder(
    array: MutableSequence,
    pivot: Any,
    left: int,
    right: int,
    cmp_func=lambda a, b: a - b,
):
    """Reorders array items (from left to right) to make elements less than pivot in left part of array, bigger - in the right part.
    CPU - O(n=right-left)
    RAM - O(1)"""
    left_copy = left
    right_copy = right
    while right_copy > left_copy:
        if left >= right:
            break
        while cmp_func(array[left_copy], pivot) <= -1:
            left_copy += 1
        while cmp_func(array[right_copy], pivot) >= 1:
            right_copy -= 1
        array[left_copy], array[right_copy] = array[right_copy], array[left_copy]
    center = None
    left_copy = left
    right_copy = right
    while left_copy <= right_copy:
        if array[left_copy] == pivot:
            center = left_copy
        left_copy += 1
    return center


def quicksort(
    array: MutableSequence,
    cmp_func=lambda a, b: a - b,
    left: int = None,
    right: int = None,
):
    """Inplace quicksort.
    CPU - O(n log(n))
    RAM - O(log(n))

    :param array: array with unique items to sort.
    :param cmp_func: function that compares two items.
    :param left: left border of an input array.
    :param right: right border of an input array.
    """
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if left >= right:
        return
    pivot = find_pivot(array, left, right)
    center = reorder(array, pivot, left, right, cmp_func)
    quicksort(array, cmp_func, left, center - 1)
    quicksort(array, cmp_func, center + 1, right)


def cmp(a: tuple[int, int, str], b: tuple[int, int, str]):
    if a[0] < b[0]:
        return 1
    elif a[0] > b[0]:
        return -1

    if a[1] < b[1]:
        return -1
    elif a[1] > b[1]:
        return 1

    if a[2] < b[2]:
        return -1
    elif a[2] > b[2]:
        return 1

    return 0


def main():
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        n = inp.readline()
        n = int(n)
        array = []
        for i in range(n):
            line = inp.readline()
            data = line.split()
            array.append((int(data[1]), int(data[2]), data[0]))
        quicksort(array, cmp)
        print(*map(lambda x: x[2], array), sep="\n", file=outp)


if __name__ == "__main__":
    main()
