def solve(children, cookies):
    """CPU - O(n log(n))
    RAM - O(1)"""
    res = 0
    children.sort()
    cookies.sort()
    child = 0
    for cookie in cookies:
        if child >= len(children):
            break
        if cookie >= children[child]:
            child += 1
            res += 1
    return res


def main():
    """CPU - O(n log(n))
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        children = list(map(int, inp.readline().strip().split()))
        m = int(inp.readline())
        cookies = list(map(int, inp.readline().strip().split()))
        res = solve(children, cookies)
        print(res, file=outp)


if __name__ == "__main__":
    main()
