import itertools

BUTTONS = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
}


def parse_input(input_file):
    val = input_file.readline()
    res = []
    for el in val:
        res.append(BUTTONS[int(el)])
    return res


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        input_data = parse_input(inp)
        print(*map(lambda x: "".join(x), itertools.product(*input_data)), file=outp)


if __name__ == "__main__":
    main()
