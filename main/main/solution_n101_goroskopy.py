def main():
    n, a, m, b = open("input.txt").read().splitlines()[:4]
    a = a.split()
    b = b.split()
    n, m = int(n), int(m)
    d = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(1, len(d)):
        for j in range(1, len(d[i])):
            if a[i - 1] == b[j - 1]:
                d[i][j] = d[i - 1][j - 1] + 1
            else:
                d[i][j] = max(d[i - 1][j], d[i][j - 1])
    print(d[-1][-1])
    c = []
    while d[n][m] > 0:
        if a[n - 1] == b[m - 1]:
            c.append((n, m))
            n -= 1
            m -= 1
        elif d[n][m] == d[n][m - 1]:
            m -= 1
        else:
            n -= 1
    a, b = zip(*reversed(c)) if len(c) > 0 else ([], [])
    print(*a)
    print(*b)


if __name__ == "__main__":
    main()
