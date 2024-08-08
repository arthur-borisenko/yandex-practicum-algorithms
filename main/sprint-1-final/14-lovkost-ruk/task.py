def solve(k, field):
    """CPU - O(n)
    n - field size
    RAM-O(m)
    m - number of different digits"""
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
    n - field size, in current task - 16
    RAM-O(m)
    m - number of different digits, in current task, can be from 1 to 9
    :return: Void
    """
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        k = int(inp.readline())
        field = inp.read()
        print(solve(k, field), file=outp)


if __name__ == "__main__":
    main()
