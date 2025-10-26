def main():
    """CPU - O(n)
    RAM - O(n)"""
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = inp.readline()
        d = []
        occurrences = {}
        for i in range(int(n)):
            line = inp.readline().strip().rstrip()
            occurrences[line] = occurrences.get(line, 0) + 1
            if occurrences.get(line, 0) == 1:
                print(line, file=out)


if __name__ == "__main__":
    main()
