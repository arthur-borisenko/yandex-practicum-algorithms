def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        m = {}
        uniq = 0
        n, k = map(int, inp.readline().split())
        for i in range(k):
            ribble = inp.readline()
            v1, v2 = map(int, ribble.split())
            if v1 == v2:
                continue
            m[v1] = m.get(v1, {})
            m[v2] = m.get(v2, {})
            if v2 not in m[v1]:
                m[v1][v2] = 1
                m[v2][v1] = 1
                uniq += 1
        print("YES" if uniq == n * (n - 1) / 2 else "NO", file=out)


if __name__ == "__main__":
    main()
