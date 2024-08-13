def fibonacci_number(n):
    f = 1
    prev_f = 1
    for i in range(n - 1):
        f, prev_f = f + prev_f, f
    return f


def main():
    """CPU - O(n)
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n, k = map(int, inp.readline().split())
        print(fibonacci_number(n) % (10**k), file=outp)


if __name__ == "__main__":
    main()
