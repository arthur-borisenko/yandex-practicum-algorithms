def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n, m = map(int, inp.readline().split())
        inp2 = inp.readline().split()
        inp1 = list(zip(map(int, inp2), map(int, inp2)))
        d0 = [0 for _ in range(m)]
        for i in range(n):
            d1 = [0 for _ in range(m)]
            for j in range(1, m + 1):
                nt = d0[j - 1] if i > 0 else 0
                t_mw = j - inp1[i][0]
                t = (
                    ((inp1[i][1]) + (d0[t_mw - 1] if i > 0 and t_mw > 0 else 0))
                    if t_mw >= 0
                    else 0
                )
                if t > nt:
                    d1[j - 1] = t
                else:
                    d1[j - 1] = nt
            d0 = d1
        print(d0[-1] if len(d0) > 0 else 0, file=out)


if __name__ == "__main__":
    main()
