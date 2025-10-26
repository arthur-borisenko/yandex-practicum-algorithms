import array
import math


def array_iterator(arr):
    i = 0
    while i < len(arr):
        yield arr[i]
        i += 1


def main():
    """
    CPU - O(n)
    RAM - o(n)
    :return: Void
    """
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        res = array.array(
            "l"
        )  # using arrayList because we don't know output length, not using list because saving only primitives
        for i in range(2, int(math.sqrt(n)) + 1):
            while n % i == 0:
                res.append(i)
                n = int(n / i)
        if n > 1:
            res.append(n)
        print(" ".join(map(str, array_iterator(res))), file=outp)


if __name__ == "__main__":
    main()
