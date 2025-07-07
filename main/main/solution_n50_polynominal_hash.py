def polynominal_hash(s, base, mod):
    r = 0
    for char in s:
        code = ord(char)
        r = (base * r + code) % mod
    return r % mod


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        base, mod, s = int(inp.readline()), int(inp.readline()), inp.readline()
        print(polynominal_hash(s.strip().rstrip(), base, mod), file=out)


if __name__ == "__main__":
    main()
