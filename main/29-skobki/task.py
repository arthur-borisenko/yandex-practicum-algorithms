def gen_brackets(n, prefix, bracket, non_closed, output_file):
    prefix += bracket
    non_closed = non_closed + 1 if bracket == "(" else non_closed - 1
    if n - 1 == 0:
        if non_closed == 0:
            print(prefix, file=output_file)
    else:
        gen_brackets(n - 1, prefix, "(", non_closed, output_file)
        if non_closed > 0:
            gen_brackets(n - 1, prefix, ")", non_closed, output_file)


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        total = int(inp.readline()) * 2
        gen_brackets(total, "", "(", 0, outp)


if __name__ == "__main__":
    main()
