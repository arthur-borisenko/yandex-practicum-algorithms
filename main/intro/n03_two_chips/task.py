def main():
    with open("input.txt") as input_file, open("output.txt", "w") as output_file:
        n = int(input_file.readline())
        l = list(map(int, input_file.readline().split()))
        k = int(input_file.readline())
        res = None
        for i in range(n - 1):
            for j in range(i + 1, n):
                a, b = l[i], l[j]
                if a + b == k:
                    res = (a, b)
                    break
        print(*res if res else (res,), file=output_file)


if __name__ == "__main__":
    main()
