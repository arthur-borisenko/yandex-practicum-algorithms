def knapsack(half_sum, l, n):
    d0 = [0 for _ in range(half_sum)]
    for i in range(n):
        d1 = [0 for _ in range(half_sum)]
        for j in range(1, half_sum + 1):
            not_take = d0[j - 1] if i > 0 else 0
            t_mw = j - l[i]
            take = (
                ((l[i]) + (d0[t_mw - 1] if i > 0 and t_mw > 0 else 0))
                if t_mw >= 0
                else 0
            )
            if take > not_take:
                d1[j - 1] = take
            else:
                d1[j - 1] = not_take
        d0 = d1
    return d0


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        l = list(map(int, inp.readline().split()))
        s = sum(l)
        if s % 2 == 0:
            half_sum = s // 2
            d0 = knapsack(half_sum, l, n)
            print(d0[-1] == half_sum, file=out)

        else:
            print(False, file=out)


if __name__ == "__main__":
    main()
