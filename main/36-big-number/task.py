import functools


def compare(a, b):
    if a > b:
        return 1
    if a < b:
        return -1
    else:
        return 0


def cmp(x, y):
    return compare(x + y, y + x)


def main():
    """CPU - O(n**2)
    RAM - O(1)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        inp_data = inp.readline().split()
        res = sorted(inp_data, key=functools.cmp_to_key(cmp), reverse=True)
        print(*res, sep="", file=outp)


if __name__ == "__main__":
    main()
