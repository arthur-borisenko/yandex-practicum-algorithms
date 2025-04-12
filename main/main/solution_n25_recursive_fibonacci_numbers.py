def recursive_fibonacci_numbers(i, n, prev_prev_f, prev_f):
    if i > n:
        return prev_f
    else:
        current_f = prev_prev_f + prev_f
        return recursive_fibonacci_numbers(i + 1, n, prev_f, current_f)


def main():
    """CPU - O(n)
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        print(recursive_fibonacci_numbers(2, n, 1, 1), file=outp)


if __name__ == "__main__":
    main()
