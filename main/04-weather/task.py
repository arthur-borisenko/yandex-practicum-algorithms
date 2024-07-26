def main():
    with open("input.txt") as inp, open("output.txt", "w") as of:
        n = int(inp.readline())
        temps = list(map(int, inp.readline().split()))
        normal = 0
        for i in range(n):
            if i > 0:
                if temps[i - 1] >= temps[i]:
                    normal += 1
                    continue
            if i + 1 < n:
                if temps[i + 1] >= temps[i]:
                    normal += 1
                    continue
        print(n - normal, file=of)


if __name__ == "__main__":
    main()
