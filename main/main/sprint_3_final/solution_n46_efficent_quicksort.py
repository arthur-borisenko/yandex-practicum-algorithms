def find_pivot(array, left, right):
    return sorted((array[left + (right - left) // 2], array[left], array[right]))[1]


def reorder(array, pivot, left, right, cmp_func):
    """Reorders array items to make elements less than pivot in left part of array, bigger - in the right part.
    CPU - O(n)
    RAM - O(1)"""
    left1 = left
    right1 = right
    while right > left:
        if left >= right:
            break
        while cmp_func(array[left], pivot) == -1:
            left += 1
        while cmp_func(array[right], pivot) == 1:
            right -= 1
        array[left], array[right] = array[right], array[left]
    center = None
    while left1 <= right1:
        if array[left1] == pivot:
            center = left1
        left1+=1
    return center


def quicksort(array, left, right, cmp_func):
    """Inplace quicksort.
    CPU - O(n log(n))
    RAM - O(log(n))
    array - array with unique items.
    cmp_func - function that compares two items."""
    if left >= right:
        return
    pivot = find_pivot(array, left, right)
    center = reorder(array, pivot, left, right, cmp_func)
    quicksort(array, left, center - 1, cmp_func)
    quicksort(array, center + 1, right, cmp_func)

def cmp(a, b):
    n1, p1, f1, n2, p2, f2 = a[0], a[1], a[2], b[0], b[1], b[2]
    if p1 < p2:
        return 1
    if p1 > p2:
        return -1
    if f1 < f2:
        return -1
    if f1 > f2:
        return 1
    if n1 < n2:
        return -1
    if n1 > n2:
        return 1
    return 0


def main():
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        n = inp.readline()
        n = int(n)
        array = []
        for i in range(n):
            line = inp.readline()
            array.append((line.split()[0], int(line.split()[1]), int(line.split()[2])))
        quicksort(array, 0, n - 1, cmp)
        print(*map(lambda x: x[0], array), sep="\n", file=outp)


if __name__ == "__main__":
    main()
