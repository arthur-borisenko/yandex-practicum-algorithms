def recursive_fibonacci_numbers(n, cache):
    if cache.get(n, None) is None:
        fib_n = recursive_fibonacci_numbers(n - 1, cache) + recursive_fibonacci_numbers(
            n - 2, cache
        )
        cache[n] = fib_n
    else:
        fib_n = cache[n]
    return fib_n


def main():
    """CPU - O(n)
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        cache = {0: 1, 1: 1}
        print(recursive_fibonacci_numbers(n, cache), file=outp)


if __name__ == "__main__":
    main()
