def main():
    with open("input.txt") as inp, open("output.txt", "w") as of:
        n = int(inp.readline())
        m = int(inp.readline())
        matrix = []
        for i in range(n):
            matrix.append(list(map(int, inp.readline().split())))
        x = int(inp.readline())
        y = int(inp.readline())
        result = []
        if x > 0:
            result.append(matrix[x - 1][y])
        if x < n - 1:
            result.append(matrix[x + 1][y])
        if y > 0:
            result.append(matrix[x][y - 1])
        if y < m - 1:
            result.append(matrix[x][y + 1])
        print(*sorted(result), file=of)


if __name__ == "__main__":
    main()
