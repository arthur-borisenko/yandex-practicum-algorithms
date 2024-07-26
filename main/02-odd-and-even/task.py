def is_even(n):
    return n % 2 == 0


def main():
    with open("input.txt") as f:
        inp = f.readline()
    a, b, c = tuple(map(int, inp.split()))
    with open("output.txt", "w") as f:
        print("WIN" if is_even(a) == is_even(b) == is_even(c) else "FAIL", file=f)


if __name__ == "__main__":
    main()
