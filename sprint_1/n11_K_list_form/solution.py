import array


def main():
    """
    CPU - O(n)
    RAM - o(n)
    :return: Void
    """
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        x_len = int(inp.readline())
        x = tuple(map(int, inp.readline().split()))
        k = array.array("i", map(int, inp.readline().strip()))
        res = array.array("i", [0] * (max(len(x), len(k)) + 1))
        next_add = False
        for i in range(max(len(x), len(k))):
            summ = (
                (x[-i - 1] if len(x) > i else 0)
                + (k[-i - 1] if len(k) > i else 0)
                + (1 if next_add else 0)
            )
            next_add = False
            res[-i - 1] = summ % 10
            if summ >= 10:
                next_add = True
        if next_add:
            res[0] = 1
            print(*res, file=outp)
        else:
            print(*res[1:], file=outp)


if __name__ == "__main__":
    main()
