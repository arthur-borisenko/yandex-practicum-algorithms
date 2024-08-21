import array


def count_sort_o_max_min(arr, reverse=False):
    """CPU - O(n+max(arr)-min(arr))
    RAM - O(n)"""
    counts = array.array("q", [0] * (max(arr) + 1))
    for el in arr:
        counts[el] = counts[el] + 1
    res = array.array("q", [0] * len(arr))
    index = 0
    for i in range(min(arr), max(arr) + 1):
        for j in range(counts[i]):
            res[index] = i
            index += 1
    return array.array("q", reversed(res)) if reverse else res


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
