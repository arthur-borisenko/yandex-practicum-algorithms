MAX_NUMBER = 10000


def main():
    """
    CPU - O(log4(n))
    RAM - O(1)
    :return: Void
    """
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        res = False
        next_power = 1
        while next_power < MAX_NUMBER:
            if next_power == n:
                res = True
            next_power *= 4
        print(str(res), file=outp)


if __name__ == "__main__":
    main()
