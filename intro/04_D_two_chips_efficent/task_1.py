def main():
    with open("input.txt") as inp, open("output.txt", "w") as of:
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
        print(*res if res else (res,), file=of)


if __name__ == "__main__":
    main()
