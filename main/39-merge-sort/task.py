def _merge(arr1, arr2):
    res = [0] * (len(arr1) + len(arr2))
    append_i = 0
    arr1_i, arr2_i = 0, 0
    for i in range(len(arr1) + len(arr2)):
        if arr1_i < len(arr1) and arr2_i < len(arr2):
            if arr1[arr1_i] <= arr2[arr2_i]:
                res[append_i] = arr1[arr1_i]
                append_i += 1
                arr1_i += 1
            else:
                res[append_i] = arr2[arr2_i]
                append_i += 1
                arr2_i += 1
        elif arr2_i < len(arr2):
            res[append_i] = arr2[arr2_i]
            append_i += 1
            arr2_i += 1
        else:
            res[append_i] = arr1[arr1_i]
            append_i += 1
            arr1_i += 1
    return res


def _merge_sort(arr, lf, rg):
    interval = arr[lf:rg]
    if len(interval) == 0 or len(interval) == 1:
        return interval
    left = (0, len(interval) // 2)
    right = (len(interval) // 2, len(interval))
    sorted_left, sorted_right = _merge_sort(interval, *left), _merge_sort(
        interval, *right
    )
    return _merge(sorted_left, sorted_right)


def merge(arr, lf, mid, rg):
    left = arr[lf:mid]
    right = arr[mid:rg]
    return _merge(left, right)


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
