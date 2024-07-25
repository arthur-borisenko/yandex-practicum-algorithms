def main():
    inp = open("input.txt")
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
    of = open("output.txt", "w")
    print(*res if res else (res,), file=of)
    of.close()
    inp.close()


if __name__ == "__main__":
    main()
