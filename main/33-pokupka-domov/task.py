def solve(homes, money):
    res = 0
    current_money = money
    sorted_homes = sorted(homes)
    for home in sorted_homes:
        if current_money >= home:
            current_money -= home
            res += 1
    return res


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n, money = map(int, inp.readline().split())
        homes = list(map(int, inp.readline().strip().split()))
        print(solve(homes, money), file=outp)


if __name__ == "__main__":
    main()
