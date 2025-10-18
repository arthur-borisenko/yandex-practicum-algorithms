def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        m = 10**9 + 7
        prev_1 = 1
        prev_2 = 1
        current = 1
        for i in range(2, n + 1):
            current = (prev_1 + prev_2) % m
            prev_2 = prev_1
            prev_1 = current
        print(current, file=out)


if __name__ == "__main__":
    main()
