def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as out:
        m = int(inp.readline())
        n = int(inp.readline())
        dd = sorted(map(int, inp.readline().split()))
        ddd = [[-1 for _ in range(n)] for _ in range(m + 1)]
        ddd[0] = [1 for _ in range(n)]
        for i in range(1, m + 1):
            for j in range(n):
                rr = 0
                for k, d in enumerate(dd):
                    if k > j or i < d or ddd[i - d][k] == -1:
                        continue
                    rr += ddd[i - d][k]
                ddd[i][j] = rr
        print(ddd[-1][-1], file=out)


if __name__ == "__main__":
    main()
