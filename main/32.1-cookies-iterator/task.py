import array


def count_sort_output_parse_iterator(counts, shift=0, reverse=False):
    for i in (
        range(shift, len(counts) + shift)
        if not reverse
        else range(max(counts) + 1, shift, -1)
    ):
        for j in range(counts[i - shift]):
            yield i


def count_sort(arr):
    """CPU - O(n+max(arr))
    RAM - O(n+max(arr))"""
    shift = min(arr)
    counts = array.array("q", [0] * (max(arr) - shift + 1))
    for el in arr:
        counts[el - shift] += 1
    return count_sort_output_parse_iterator(counts, shift)


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
