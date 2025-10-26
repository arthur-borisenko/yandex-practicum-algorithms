def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        a, b = inp.readline().strip().rstrip(), inp.readline().strip().rstrip()
        dd = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
        for i in range(len(a) + 1):
            for j in range(len(b) + 1):
                if i == 0 and j == 0:
                    dd[i][j] = 0
                elif i == 0:
                    dd[i][j] = dd[i][j - 1] + 1
                elif j == 0:
                    dd[i][j] = dd[i - 1][j] + 1
                else:
                    replace_or_equal = dd[i - 1][j - 1] + (
                        1 if a[i - 1] != b[j - 1] else 0
                    )
                    remove = dd[i - 1][j] + 1
                    add = dd[i][j - 1] + 1
                    dd[i][j] = min(add, remove, replace_or_equal)
        print(dd[-1][-1], file=out)


if __name__ == "__main__":
    main()
