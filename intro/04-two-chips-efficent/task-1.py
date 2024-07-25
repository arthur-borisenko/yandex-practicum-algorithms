def main():
    inp = open("input.txt")
    n = int(inp.readline())
    l = list(map(int, inp.readline().split()))
    x = int(inp.readline())
    res = None
    prev = set()
    for el in l:
        if x - el in prev:
            res = el, x - el
            break
        prev.add(el)
    of = open("output.txt", "w")
    print(*res if res else (res,), file=of)
    of.close()
    inp.close()


if __name__ == "__main__":
    main()
