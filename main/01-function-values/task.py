def calc_func(a, x, b, c):
    return a * x**2 + b * x + c


def main():
    with open("input.txt") as inp, open("output.txt", "w") as of:
        vals = list(map(int, inp.readline().split()))
        print(calc_func(vals[0], vals[1], vals[2], vals[3]), file=of)


if __name__ == "__main__":
    main()
