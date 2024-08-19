def solve(children, cookies):
    res = 0
    sorted_children, sorted_cookies = sorted(children), sorted(cookies)
    child = 0
    for cookie in sorted_cookies:
        if child >= len(sorted_children):
            break
        if cookie >= sorted_children[child]:
            child += 1
            res += 1
    return res


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        children = list(map(int, inp.readline().strip().split()))
        m = int(inp.readline())
        cookies = list(map(int, inp.readline().strip().split()))
        res = solve(children, cookies)
        print(res, file=outp)


if __name__ == "__main__":
    main()
