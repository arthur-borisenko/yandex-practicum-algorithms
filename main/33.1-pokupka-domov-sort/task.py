def count_sort_o_max_min(arr):
    """CPU - O(n+max(arr)-min(arr))
    RAM - O(n)"""
    counts = {}
    for el in arr:
        counts[el] = counts.get(el, 0) + 1
    res = []
    for i in range(min(arr), max(arr) + 1):
        for j in range(counts.get(i, 0)):
            res.append(i)
    return res


def solve(homes, money):
    res = 0
    current_money = money
    sorted_homes = count_sort_o_max_min(homes)
    for home in sorted_homes:
        if current_money >= home:
            current_money -= home
            res += 1
    return res


def main():
    """CPU - O(n+max(arr)-min(arr))
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n, money = map(int, inp.readline().split())
        homes = list(map(int, inp.readline().strip().split()))
        print(solve(homes, money), file=outp)


if __name__ == "__main__":
    main()
