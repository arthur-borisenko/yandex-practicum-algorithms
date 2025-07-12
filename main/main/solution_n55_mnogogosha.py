base = 10**9 + 7
mod = 10**18 + 3


def polynominal_hash(s, base, mod):
    """CPU - O(n)
    RAM - O(1)

    we can use result % mod on all iterations, and it will equal result%mod on last iteration because:
    result = mod * a + r,
    so r = result % mod = result - mod * a.
    On next iteration we calculate result using:
    result = (base * mod * a + base * r + code) % mod
    and because first part has multiplier a, it will give zero modulo,
    so (base * mod * a + base * r + code) % mod = (base * mod * a - base*mod*a+base*r+code)%mod
    so, because we return result % mod, we can use (base * mod * a - base * mod * a + base * r + code) % mod,
    which equals (base * (result % mod) + code) % mod in all calculations
    """
    result = 0
    for char in s:
        code = ord(char)
        result = (base * result + code) % mod
    return result


def count_substrings(n, k, x):
    fuck = pow(base, n - 1, mod)
    res = []
    h = polynominal_hash(x[:n], base, mod)
    counts = {}
    for i in range(len(x) - n):
        if i != 0:
            h = ((h - ord(x[i - 1]) * fuck) * base + ord(x[i - 1 + n])) % mod
        if h not in counts:
            counts[h] = [0, i]
        counts[h][0] += 1
    for key in counts.keys():
        if counts[key][0] >= k:
            res.append(counts[key][1])
    return res


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n, k = map(int, inp.readline().split())
        x = inp.readline()
        print(*count_substrings(n, k, x), file=out)


if __name__ == "__main__":
    main()
