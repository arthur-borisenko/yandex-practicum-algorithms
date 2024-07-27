def main():
    with open("input.txt") as input_file, open("output.txt", "w") as output_file:
        n = int(input_file.readline())
        temps = list(map(int, input_file.readline().split()))
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
        print(n - normal, file=output_file)


if __name__ == "__main__":
    main()
