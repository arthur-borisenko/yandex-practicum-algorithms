class DirEnum:
    UP = "U"
    RIGHT = "R"


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        path = []
        path2 = []
        inp1 = []
        n, m = map(int, inp.readline().split())
        for i in range(n):
            inp1.append(
                list(map(int, inp.readline().strip().rstrip())))
        d = [[0 for _ in range(m)] for _ in range(n)]

        for ii in range(-n + 1, 1):
            i = -ii
            for j in range(m):
                d[i][j] = 0
                if i + 1 < len(d):
                    d[i][j] = max(d[i][j], d[i + 1][j])
                if j > 0:
                    d[i][j] = max(d[i][j], d[i][j - 1])
                d[i][j] += inp1[i][j]
                pass
        print(d[0][-1], file=out)


if __name__ == '__main__':
    main()
