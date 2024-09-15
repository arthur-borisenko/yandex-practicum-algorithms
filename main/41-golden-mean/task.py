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
    res = float("inf")
    for seq1_i in range(len(arr1)):  # TODO: use binary search
        seq2_i = idx - seq1_i - 1
        if seq2_i < -1:
            continue
        if not is_arr_empty(arr2, seq2_i) and (
            is_arr_empty(arr2, seq2_i + 1) or arr2[seq2_i + 1] >= arr1[seq1_i]
        ):
            print(seq1_i, seq2_i)
            res = arr2[seq2_i]
    for seq2_i in range(len(arr2)):  # TODO: use binary search
        seq1_i = idx - seq2_i - 1
        if seq1_i < -1:
            continue
        if not is_arr_empty(arr1, seq1_i) and (
            is_arr_empty(arr1, seq1_i + 1) or arr1[seq1_i + 1] >= arr2[seq2_i]
        ):
            print(seq1_i, seq2_i)
            if res > arr2[seq2_i]:
                res = arr1[seq1_i]
    if res != float("inf"):
        return res
    raise Exception("Index out of range or internal error occurred")


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
