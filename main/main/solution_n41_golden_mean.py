from typing import Generator, Sequence


def safe_float_to_int(x):
    if int(x) == x:
        return int(x)
    return x


def is_arr_empty(arr, i):
    return i >= len(arr)


def merge_arrays(arr1: Sequence, arr2: Sequence) -> Generator:
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


def is_index_valid(i, seq):
    return i < len(seq) and i >= 0


def get_el_by_merged_i(arr1: Sequence, arr2: Sequence, idx):
    start = -1
    end = len(arr1) - 1
    if len(arr1) + len(arr2) <= idx:
        return -1
    if len(arr2) == 0:
        return arr1[idx]
    if len(arr1) == 0:
        return arr2[idx]
    while start <= end:
        arr1_i = (start + end) // 2
        arr2_i = idx - arr1_i - 1
        if arr2_i < -1:
            end = arr1_i - 1
        elif arr2_i >= len(arr2):
            start = arr1_i + 1
        elif arr1_i + 1 < len(arr1) and arr1[arr1_i + 1] < arr2[arr2_i]:
            start = arr1_i + 1
        elif arr1_i > -1 and arr2_i + 1 < len(arr2) and arr2[arr2_i + 1] < arr1[arr1_i]:
            end = arr1_i - 1
        else:
            if arr1_i == -1:
                return arr2[arr2_i]
            if arr2_i == -1:
                return arr1[arr1_i]
            return max(arr1[arr1_i], arr2[arr2_i])
    return -1


def solve(arr1, arr2):
    """CPU - O(n+m)
    RAM - O(1)"""
    merged_len = len(arr1) + len(arr2)
    if merged_len % 2 == 0:
        mid_i = merged_len // 2 - 1
        return (
            get_el_by_merged_i(arr1, arr2, mid_i)
            + get_el_by_merged_i(arr2, arr1, mid_i + 1)
        ) / 2
    else:
        mid_i = merged_len // 2
        return get_el_by_merged_i(arr1, arr2, mid_i)


def main():
    """CPU - O(n + m)
    RAM - O(n + m)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n, m = int(inp.readline()), int(inp.readline())
        arr1 = list(map(int, inp.readline().split()))
        arr2 = list(map(int, inp.readline().split()))
        print(safe_float_to_int(solve(arr1, arr2)), file=outp)


if __name__ == "__main__":
    main()
