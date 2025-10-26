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
    val = input_file.readline().strip()
    res = []
    for el in val:
        res.append(BUTTONS[int(el)])
    return res


def product(*iterables):
    if len(iterables) == 1:
        return list(iterables[0])
    _1 = product(*iterables[:-1])
    _2 = iterables[-1]
    res = []
    for el in _1:
        for el2 in _2:
            res.append(el + el2)
    return res


def main():
    """CPU - O(3**n)
    RAM - O(3**n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        input_data = parse_input(inp)
        print(*map(lambda x: "".join(x), product(*input_data)), file=outp)


if __name__ == "__main__":
    main()
