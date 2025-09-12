def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        m = int(inp.readline())
        n = int(inp.readline())
        dd = list(map(int, inp.readline().split()))
        ddd = [-1 for _ in range(m + 1)]
        ddd[0] = 0
        for i in range(1, m + 1):
            rr = -1
            for d in dd:
                if i < d or ddd[i - d] == -1:
                    continue
                r = ddd[i - d] + 1
                if rr == -1 or r < rr:
                    rr = r
            ddd[i] = rr
        print(ddd[-1], file=out)


if __name__ == "__main__":
    main()
