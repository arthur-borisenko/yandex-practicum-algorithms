def gen_brackets(n, prefix, opening, closing, output_file):
    if (n - 1) == 0:
        if opening == closing:
            print(prefix, file=output_file)
    else:
        gen_brackets(n - 1, prefix + "(", opening + 1, closing, output_file)
        if opening >= closing + 1:
            gen_brackets(n - 1, prefix + ")", opening, closing + 1, output_file)


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        total = int(inp.readline()) * 2
        gen_brackets(total, "(", 1, 0, outp)


if __name__ == "__main__":
    main()
