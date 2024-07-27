def main():
    with open("input.txt") as input_file, open("output.txt", "w") as output_file:
        n = int(input_file.readline())
        m = int(input_file.readline())
        matrix = []
        for i in range(n):
            matrix.append(list(map(int, input_file.readline().split())))
        x = int(input_file.readline())
        y = int(input_file.readline())
        result = []
        if x > 0:
            result.append(matrix[x - 1][y])
        if x < n - 1:
            result.append(matrix[x + 1][y])
        if y > 0:
            result.append(matrix[x][y - 1])
        if y < m - 1:
            result.append(matrix[x][y + 1])
        print(*sorted(result), file=output_file)


if __name__ == "__main__":
    main()
