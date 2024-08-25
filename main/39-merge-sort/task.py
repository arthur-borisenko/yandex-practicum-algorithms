def _merge_sort(arr, lf, rg):
    """CPU - O(n log(n))
    RAM - O(log(n))
    n - interval length"""
    interval = arr[lf:rg]
    if len(interval) == 0 or len(interval) == 1:
        return interval
    left = (0, len(interval) // 2)
    right = (len(interval) // 2, len(interval))
    sorted_left, sorted_right = _merge_sort(interval, *left), _merge_sort(
        interval, *right
    )
    arr = sorted_left.extend(sorted_right)
    merge(arr, 0, len(sorted_left), len(sorted_left) + len(sorted_right))
    return arr


def merge(arr, lf, mid, rg):
    l, r, k = 0, 0, 0
    while l < mid - lf and r < rg - mid:
        if arr[l + lf - 1] <= arr[r + mid - 1]:
            arr[k + lf - 1] = arr[l + lf - 1]
            l += 1
        else:
            arr[k + lf - 1] = arr[r + mid - 1]
            r += 1
        k += 1

    while l < mid - lf:
        arr[k + lf - 1] = arr[l + lf - 1]
        l += 1
        k += 1
    while l < rg - mid:
        arr[k + lf - 1] = arr[l + mid - 1]
        l += 1
        k += 1


def merge_sort(arr, lf, rg):
    arr[lf:rg] = _merge_sort(arr, lf, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected, f"{b} != {expected}"
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected, f"{c} != {expected}"


if __name__ == "__main__":
    test()
