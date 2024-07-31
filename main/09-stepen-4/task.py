MAX_NUMBER = 10000


def main():
    """
    CPU - O(n)
    RAM - o(n)
    :return: Void
    """
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        current_power = 0
        res = False
        while 4**current_power < MAX_NUMBER:
            if 4**current_power == n:
                res = True
            current_power += 1
        print(str(res), file=outp)


if __name__ == "__main__":
    main()
