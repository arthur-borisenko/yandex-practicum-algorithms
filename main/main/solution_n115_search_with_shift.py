def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = int(inp.readline().strip())
        dt = list(map(int, inp.readline().strip().split()))
        m = int(inp.readline().strip())
        p = list(map(int, inp.readline().strip().split()))
        pp = []
        for el in p:
            pp.append(el - p[0])
        res = []
        for si in range(n - m + 1):
            pp2 = []
            for i in range(si, si + m):
                pp2.append(dt[i] - dt[si])
            if pp == pp2:
                res.append(si + 1)
        print(*res, file=out)
if __name__ == "__main__":
    main()