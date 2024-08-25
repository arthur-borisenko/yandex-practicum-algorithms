import array


def count_sort_to_orig_arr_iterator(cnt_arr, shift=0):
    """CPU - O(n)
    RAM - O(1)
    May not be used outside count sort
    :param cnt_arr: counts array
    :param shift: minimal element of orig array
    :return: result iterator"""
    for i, cnt in enumerate(cnt_arr):
        for _ in range(cnt):
            yield i + shift


def count_sort(arr):
    """CPU - O(n+max(arr))
    RAM - O(n+max(arr))
    does not change source array
    :param arr: array to be sorted
    :return: result iterator"""
    shift = min(arr)
    counts = array.array("q", [0] * (max(arr) - shift + 1))
    for el in arr:
        counts[el - shift] += 1
    return count_sort_to_orig_arr_iterator(counts, shift)


def solve(children, cookies):
    res = 0
    sorted_children, sorted_cookies = array.array(
        "q", count_sort(children)
    ), count_sort(cookies)
    child = 0
    for cookie in sorted_cookies:
        if child >= len(sorted_children):
            break
        if cookie >= sorted_children[child]:
            child += 1
            res += 1
    return res


def main():
    """CPU - O(n+m+max(children)+max(cookies))
    RAM - O(n+m+max(children)+max(cookies))"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        children = list(map(int, inp.readline().strip().split()))
        m = int(inp.readline())
        cookies = list(map(int, inp.readline().strip().split()))
        res = solve(children, cookies)
        print(res, file=outp)


if __name__ == "__main__":
    main()
