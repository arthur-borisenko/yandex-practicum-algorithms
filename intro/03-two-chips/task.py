def main():
    with open("input.txt") as inp, open("output.txt", "w") as of:
        n = int(inp.readline())
        l = list(map(int, inp.readline().split()))
        x = int(inp.readline())
        res = None
        for i in range(n - 1):
            for j in range(i + 1, n):
                a, b = l[i], l[j]
                if a + b == x:
                    res = (a, b)
                    break
        print(*res if res else (res,), file=of)


if __name__ == "__main__":
    main()
