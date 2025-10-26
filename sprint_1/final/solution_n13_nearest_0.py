from array import array as arr


def get_distance(x1, x2):
    return abs(x1 - x2)


def solve(n, street):
    """CPU - O(k * m),
    k - number of non-0 elements
    m - number of 0 elements
    ram - O(n)"""
    res = arr("L", range(n))
    first_0 = None
    next_0 = None
    for i in range(n):
        if street[i] == "0":
            first_0 = i
        if street[i] == "0" or (first_0 is None and next_0 is None):
            for j in range(i + 1, n):
                if street[j] == "0":
                    next_0 = j
                    break
        if next_0 is None:
            res[i] = get_distance(i, first_0)
        elif first_0 is None:
            res[i] = get_distance(i, next_0)
        elif get_distance(i, first_0) <= get_distance(i, next_0):
            res[i] = get_distance(i, first_0)
        elif get_distance(i, next_0) < get_distance(i, first_0):
            res[i] = get_distance(i, next_0)
    return res


def main():
    """
    CPU - O(n)
    RAM - O(n)
    :return: Void
    """
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        street = inp.readline().split()
        print(" ".join(map(str, solve(n, street))), file=outp)


if __name__ == "__main__":
    main()
