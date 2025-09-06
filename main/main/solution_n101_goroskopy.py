def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as out:
        n, a_idcs, m, b_idcs = inp.read().splitlines()[:4]
        a_idcs = a_idcs.split()
        b_idcs = b_idcs.split()
        n, m = int(n), int(m)
        d = [[0 for _ in range(len(b_idcs) + 1)] for _ in range(len(a_idcs) + 1)]
        for i in range(1, len(d)):
            for j in range(1, len(d[i])):
                if a_idcs[i - 1] == b_idcs[j - 1]:
                    d[i][j] = d[i - 1][j - 1] + 1
                else:
                    d[i][j] = max(d[i - 1][j], d[i][j - 1])
        print(d[-1][-1], file=out)
        res = []
        while d[n][m] > 0:
            if a_idcs[n - 1] == b_idcs[m - 1]:
                res.append((n, m))
                n -= 1
                m -= 1
            elif d[n][m] == d[n][m - 1]:
                m -= 1
            else:
                n -= 1
        a_idcs, b_idcs = zip(*reversed(res)) if len(res) > 0 else ([], [])
        print(*a_idcs, file=out)
        print(*b_idcs, file=out)


if __name__ == "__main__":
    main()
