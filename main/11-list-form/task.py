import array


def main():
    """
    CPU - O(n)
    RAM - o(n)
    :return: Void
    """
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        l = int(inp.readline())
        n = tuple(map(int, inp.readline().split()))
        k = array.array("i", map(int, inp.readline().strip()))
        res = array.array("i", [0] * (max(len(n), len(k)) + 1))
        next_add = False
        for i in range(max(len(n), len(k))):
            summ = (
                (n[-i - 1] if len(n) > i else 0)
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
