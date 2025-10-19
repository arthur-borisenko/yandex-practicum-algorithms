def count_less_or_equal_differences(elements, target):
    a = 1
    b = 0
    d = 0
    for i, el in enumerate(elements):
        c = target + el
        e = d - 1 if d > 0 else 0
        a = max(a, i + 1)
        while a < len(elements) and elements[a] <= c:
            a += 1
            e += 1
        b += e
        d = e
    return b


def solution(elements, k):
    l, r = 0, elements[-1] - elements[0]
    m = r // 2
    while m >= 0:
        m = (r + l) // 2
        nm = count_less_or_equal_differences(elements, m)
        if l == r:
            return l
        elif nm < k:
            l = m + 1
        elif nm >= k:
            r = m


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        l = sorted(map(int, inp.readline().split()))
        k = int(inp.readline())
        print(solution(l, k), file=out)


if __name__ == "__main__":
    main()
