alphabet = {"b", "d", "f", "h", "j", "l", "n", "p", "r", "t", "v", "x", "z"}


def normalize(s: str) -> str:
    return "".join(x if x in alphabet else "" for x in s)


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        x = normalize(inp.readline())
        y = normalize(inp.readline())
        print(-1 if x < y else 0 if x == y else 1, file=out)


if __name__ == '__main__':
    main()