def calc_func(a, x, b, c):
    return a * x**2 + b * x + c


def main():
    with open("input.txt") as input_file, open("output.txt", "w") as output_file:
        vals = list(map(int, input_file.readline().split()))
        print(calc_func(vals[0], vals[1], vals[2], vals[3]), file=output_file)


if __name__ == "__main__":
    main()
