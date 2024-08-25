import array


def count_sort(arr, reverse=False):
    """CPU - O(n+max(arr))
    RAM - O(n+max(arr))
    sorts input array, does not return anything
    :param arr: array to sort
    :param reverse: reverse the order of the result
    :return: void"""
    counts = array.array("q", [0] * (max(arr) + 1))
    for el in arr:
        counts[el] = counts[el] + 1
    index = 0
    for i in range(min(arr), max(arr) + 1):
        for j in range(counts[i]):
            arr[index if not reverse else -index] = i
            index += 1


def solve(children, cookies):
    res = 0
    sorted_children, sorted_cookies = children.copy(), cookies.copy()
    count_sort(sorted_children)
    count_sort(sorted_cookies)
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
