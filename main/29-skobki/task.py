def next_parentheses(src):
    res = set()
    for el in src:
        res.add("()" + el)
        res.add(el + "()")
        res.add("(" + el + ")")
    return res


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        res = {""}
        for i in range(n):
            res = next_parentheses(res)
        print(*sorted(res), sep="\n", file=outp)


if __name__ == "__main__":
    main()
