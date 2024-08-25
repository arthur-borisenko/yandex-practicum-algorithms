from array import array
from typing import Any


# asc sort. non existent (e.g. []) elements not excluded
def count_sort_obj(arr: list[Any]) -> list[list[Any]]:
    min_val = min(arr)  # TODO>>may be use less memory (min to max)
    result: list[list[int]] = [[] for _ in range((max(arr) + 1))]
    for i, val in enumerate(arr):
        result[val].append(i)
    return result


# asc sort. non existent (e.g. 0) elements not excluded
def count_sort(arr: array[int]) -> array[int]:
    min_val = min(arr)  # TODO>>may be use less memory (min to max)
    result = array("q", [0] * (max(arr) + 1))
    for val in arr:
        result[val] += 1
    return result


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        stud_univer_ids = array("q", map(int, inp.readline().split()))
        k = int(inp.readline())
        stud_cnt_per_univer_id = count_sort(stud_univer_ids)
        univer_ids_per_stud_cnt = count_sort_obj(stud_cnt_per_univer_id)
        univer_ids_desc = list(
            reversed(univer_ids_per_stud_cnt[1:])
        )  # skip univers with 0 stud, then reverse - populars first
        print_output(k, univer_ids_desc, outp)


def print_output(k, arr: list[list[int]], outp):
    for i, sub_arr in enumerate(arr):
        for j, val in enumerate(sub_arr):
            print(val, end=" ", file=outp)
            k -= 1
            if k == 0:
                return


if __name__ == "__main__":
    main()
