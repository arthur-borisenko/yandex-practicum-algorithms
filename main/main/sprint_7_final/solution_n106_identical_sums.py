def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        l = list(map(int, inp.readline().split()))
        s = sum(l)
        if s % 2 == 0:
            half_sum = s // 2
            d0 = [0 for _ in range(half_sum)]
            for i in range(n):
                d1 = [0 for _ in range(half_sum)]
                for j in range(1, half_sum + 1):
                    nt = d0[j - 1] if i > 0 else 0
                    t_mw = j - l[i]
                    t = (
                        ((l[i]) + (d0[t_mw - 1] if i > 0 and t_mw > 0 else 0))
                        if t_mw >= 0
                        else 0
                    )
                    if t > nt:
                        d1[j - 1] = t
                    else:
                        d1[j - 1] = nt
                d0 = d1
            print(d0[-1] == half_sum, file=out)

        else:
            print(False, file=out)


if __name__ == "__main__":
    main()
