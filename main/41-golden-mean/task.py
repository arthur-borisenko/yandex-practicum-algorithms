def safe_float_to_int(x):
    if int(x) == x:
        return int(x)
    return x


def is_arr_empty(arr, i):
    return i >= len(arr)


def merge_arrays(arr1, arr2):
    """
    CPU - O(1)
    RAM - O(1)
    :param arr1: first array of comparable objects in ascending order
    :param arr2: second array of comparable objects in ascending order
    :return: iterator of merged arrays in ascending order
    """
    arr1_i, arr2_i = 0, 0

    for i in range(len(arr1) + len(arr2)):
        if (not is_arr_empty(arr1, arr1_i)) and (
            is_arr_empty(arr2, arr2_i) or arr1[arr1_i] <= arr2[arr2_i]
        ):
            yield arr1[arr1_i]
            arr1_i += 1
        else:
            yield arr2[arr2_i]
            arr2_i += 1


def solve(arr1, arr2):
    """CPU - O(n+m)
    RAM - O(1)"""
    merged_len = len(arr1) + len(arr2)
    merged = merge_arrays(arr1, arr2)
    if merged_len % 2 == 0:
        left_mid_i = merged_len // 2 - 1
        for i in range(left_mid_i):
            next(merged)
        left_mid = next(merged)
        right_mid = next(merged)
        return (left_mid + right_mid) / 2
    else:
        mid_i = merged_len // 2
        for i in range(mid_i):
            next(merged)
        mid = next(merged)
        return mid


def main():
    """CPU - O(n + m)
    RAM - O(n + m)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n, m = int(inp.readline()), int(inp.readline())
        arr1, arr2 = list(map(int, inp.readline().split())), list(
            map(int, inp.readline().split())
        )
        print(safe_float_to_int(solve(arr1, arr2)), file=outp)


if __name__ == "__main__":
    main()
