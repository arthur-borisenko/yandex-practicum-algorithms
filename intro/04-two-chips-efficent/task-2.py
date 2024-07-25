def main():
    inp = open("input.txt")
    n = int(inp.readline())
    l = sorted(list(map(int, inp.readline().split())))
    x = int(inp.readline())
    res = None
    li = 0
    ri = n - 1
    for i in range(n - 1):
        if l[li] + l[ri] == x:
            res = (l[li], l[ri])
            break
        elif l[li] + l[ri] < x:
            li += 1
        else:
            ri -= 1
    of = open("output.txt", "w")
    print(*res if res else (res,), file=of)
    of.close()
    inp.close()


if __name__ == "__main__":
    main()
