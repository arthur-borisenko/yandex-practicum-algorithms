def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        l = list(map(int, inp.readline().split()))
        x = l
        p0 = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            max_val = 0
            p1 = [0 for _ in range(n + 1)]
            for j in range(1, n + 1):
                p1[j] = p0[j]
                if x[i - 1] == x[j - 1]:
                    p1[j] = max(p1[j], max_val + 1)
                if x[j - 1] < x[i - 1]:
                    max_val = max(max_val, p0[j])
            p0 = p1
        r = []
        mx = 0
        ii = 0
        for i, el in enumerate(p0):
            if el > mx:
                mx = el
                ii = i
        pv = mx + 1
        while ii > 0:
            if p0[ii] == pv - 1:
                r.append(ii)
                pv = p0[ii]
            ii -= 1
        print(mx, file=out)
        print(*reversed(r), file=out)


if __name__ == "__main__":
    main()
