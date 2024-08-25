import array
from typing import MutableSequence


def count_sort(arr: MutableSequence[int]) -> None:
    """CPU - O(n+max(arr))
    RAM - O(max(arr))
    sort input array of ints (non-negative) with "count sort"
    """
    counts = array.array("q", [0] * (max(arr) + 1))
    for val in arr:
        counts[val] = counts[val] + 1
    index = 0
    for i, cnt in enumerate(counts):
        for _ in range(cnt):
            arr[index] = i
            index += 1


def solve(children, cookies):
    """CPU - O(n+m+max(children)+max(cookies))
    RAM - O(max(children)+max(cookies))"""
    res = 0
    count_sort(children)
    count_sort(cookies)
    child = 0
    for cookie in cookies:
        if child >= len(children):
            break
        if cookie >= children[child]:
            child += 1
            res += 1
    return res


def main():
    """CPU - O(n+m+max(children)+max(cookies)
    RAM - O(n+m+max(children)+max(cookies)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        children = list(map(int, inp.readline().strip().split()))
        m = int(inp.readline())
        cookies = list(map(int, inp.readline().strip().split()))
        res = solve(children, cookies)
        print(res, file=outp)


if __name__ == "__main__":
    main()
