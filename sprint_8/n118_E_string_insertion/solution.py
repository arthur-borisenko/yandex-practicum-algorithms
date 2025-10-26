def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        s = inp.readline().strip()
        n = int(inp.readline().strip())
        ts = {}
        for i in range(n):
            a, b = inp.readline().strip().split()
            ts[int(b)] = a
        res = []
        if 0 in ts:
            res.append(ts[0])
        for i, ss in enumerate(s):
            res.append(ss)
            if i + 1 in ts:
                res.append(ts[i + 1])
        print("".join(res), file=out)


if __name__ == "__main__":
    main()
