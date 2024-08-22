import array


def count_sort_o_max_min(arr, reverse=False):
    """CPU - O(n+max(arr))
    RAM - O(n+max(arr))"""
    new_arr = array.array("q", arr)
    if len(new_arr) == 0:
        return []
    counts = array.array("q", [0] * (max(new_arr) + 1))
    for el in arr:
        counts[el] = counts[el] + 1
    res = array.array("q", [0] * len(new_arr))
    index = 0
    for i in range(min(arr), max(arr) + 1):
        for j in range(counts[i]):
            res[index] = i
            index += 1
    return array.array("q", reversed(res)) if reverse else res


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        items = list(map(int, inp.readline().strip().split()))
        print(*count_sort_o_max_min(items), file=outp)


if __name__ == "__main__":
    main()
