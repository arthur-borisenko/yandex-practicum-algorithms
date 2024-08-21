import array


def count_sort_o_max_min(arr, reverse=False):
    """CPU - O(n+max(arr))
    RAM - O(n+max(arr))"""
    counts = array.array("q", [0] * (max(arr) + 1))
    for el in arr:
        counts[el] = counts[el] + 1
    res = array.array("q", [0] * len(arr))
    index = 0
    for i in range(min(arr), max(arr) + 1):
        for j in range(counts[i]):
            res[index] = i
            index += 1
    return array.array("q", reversed(res)) if reverse else res


def solve(children, cookies):
    res = 0
    sorted_children, sorted_cookies = count_sort_o_max_min(
        children
    ), count_sort_o_max_min(cookies)
    child = 0
    for cookie in sorted_cookies:
        if child >= len(sorted_children):
            break
        if cookie >= sorted_children[child]:
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
