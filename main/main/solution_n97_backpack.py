def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n, m = map(int, inp.readline().split())
        inp1 = []
        for i in range(n):
            ms, cs = inp.readline().split()
            mi, ci = int(ms), int(cs)
            inp1.append((mi, ci, i))
        d1 = [[0 for _ in range(m)] for _ in range(n)]
        d2 = [[[] for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(1, m + 1):
                nt = d1[i - 1][j - 1] if i > 0 else 0
                t_mw = j - inp1[i][0]
                t = (
                    ((inp1[i][1]) + (d1[i - 1][t_mw - 1] if i > 0 and t_mw > 0 else 0))
                    if t_mw >= 0
                    else 0
                )
                if t > nt:
                    d1[i][j - 1] = t
                    d2[i][j - 1] = (
                        d2[i - 1][t_mw - 1].copy() if i > 0 and t_mw > 0 else []
                    )
                    d2[i][j - 1].append((inp1[i]))
                else:
                    d1[i][j - 1] = nt
                    d2[i][j - 1] = d2[i - 1][j - 1].copy()
                pass
        print(len(d2[-1][-1]), file=out)
        print(*map(lambda x: x[2] + 1, d2[-1][-1]), file=out)


if __name__ == "__main__":
    main()
