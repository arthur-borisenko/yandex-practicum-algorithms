def prefix_hashes(s, base, mod):
    res = [0]
    for el in s:
        res.append((res[-1] * base + ord(el)) % mod)
    return res


def precompute_powers(base, exp, mod):
    powers = [1]
    for _ in range(exp):
        powers.append((powers[-1] * base) % mod)
    return powers


def precompute(s, base, mod):
    powers = precompute_powers(base, len(s), mod)
    prefixes = prefix_hashes(s, base, mod)
    return powers, prefixes


def subhash(mod, left, right, powers, prefixes):
    return (
        prefixes[right + 1] - prefixes[left] * powers[(right - left + 1)] + mod
    ) % mod


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        base = int(inp.readline())
        mod = int(inp.readline())
        s = inp.readline()
        powers, prefixes = precompute(s, base, mod)
        t = int(inp.readline())
        for i in range(t):
            line = inp.readline().split()
            left = int(line[0]) - 1
            right = int(line[1]) - 1
            print(subhash(mod, left, right, powers, prefixes), file=out)


if __name__ == "__main__":
    main()
