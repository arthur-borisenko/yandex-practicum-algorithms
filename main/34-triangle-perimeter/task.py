def solve(lines):
    sorted_lines = sorted(lines, reverse=True)
    for i in range(2, len(sorted_lines)):
        if sorted_lines[i - 2] < sorted_lines[i - 1] + sorted_lines[i]:
            return sorted_lines[i - 2] + sorted_lines[i - 1] + sorted_lines[i]
    return -1


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        lines = list(map(int, inp.readline().strip().split()))
        print(solve(lines), file=outp)


if __name__ == "__main__":
    main()
