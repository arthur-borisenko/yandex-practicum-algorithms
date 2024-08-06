def solve(k, field):
    button_counts = {}
    for val in tuple(field):
        if val.isdigit():
            button_counts[val] = button_counts.get(val, 0) + 1
    res = 0
    for count in button_counts.values():
        if count <= k * 2:
            res += 1
    return res


def main():
    """
    CPU - O(n)
    RAM - O(n)
    :return: Void
    """
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        k = int(inp.readline())
        field = inp.read()
        print(solve(k, field), file=outp)


if __name__ == "__main__":
    main()
