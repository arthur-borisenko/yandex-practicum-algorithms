def fibonacci_number(n):
    prev_f = 1
    prev_prev_f = 1
    current_f = prev_f
    for i in range(n - 1):
        current_f = prev_f + prev_prev_f
        prev_prev_f = prev_f
        prev_f = current_f
    return current_f


def main():
    """CPU - O(n)
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n, k = map(int, inp.readline().split())
        print(fibonacci_number(n) % (10**k), file=outp)


if __name__ == "__main__":
    main()
