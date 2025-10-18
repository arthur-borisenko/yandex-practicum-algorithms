def prefix_function(s):
    n = len(s)
    prefix_func = [None] * n
    prefix_func[0] = 0
    for i in range(1, n):
        k = prefix_func[i - 1]
        while k > 0 and s[k] != s[i]:
            k = prefix_func[k - 1]
        if s[k] == s[i]:
            k += 1
        prefix_func[i] = k
    return prefix_func


def findall(s, p):
    sep = chr(31)
    c = p + sep + s
    pf = prefix_function(c)
    idcs = []
    for i in range(len(pf)):
        if pf[i] == len(p):
            idcs.append(i - 2 * len(p))
    return idcs


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        x, p, r = inp.readline().strip(), inp.readline().strip(), inp.readline().strip()
        idcs = findall(x, p)
        parts = []
        prev_i = 0
        for i in idcs:
            parts.append(x[prev_i:i])
            prev_i = i + len(p)
            parts.append(r)
        parts.append(x[prev_i : len(x)])
        print("".join(parts), file=out)


if __name__ == "__main__":
    main()
