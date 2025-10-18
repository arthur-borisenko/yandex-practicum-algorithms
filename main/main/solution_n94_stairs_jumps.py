def aaa(d, v, k, m):
    x = 0
    for i in range(max(0, v - k), v):
        x += d[i] % m
    return x % m


def dp(v, k, m):
    d = [1]
    for i in range(0, v):
        if i < len(d):
            continue
        d.append(aaa(d, i, k, m))
    return d[-1]


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        print(dp(*map(int, inp.readline().split()), 10**9 + 7), file=out)


if __name__ == "__main__":
    main()
