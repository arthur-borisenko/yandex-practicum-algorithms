def count_sort_o_max_min(arr, reverse=False):
    """CPU - O(n+max(arr)-min(arr))
    RAM - O(n)"""
    counts = {}
    for el in arr:
        counts[el] = counts.get(el, 0) + 1
    res = []
    for i in range(min(arr), max(arr) + 1):
        for j in range(counts.get(i, 0)):
            res.append(i)
    return list(reversed(res)) if reversed else res


def solve(lines):
    sorted_lines = count_sort_o_max_min(lines, reverse=True)
    for i in range(2, len(sorted_lines)):
        if sorted_lines[i - 2] < sorted_lines[i - 1] + sorted_lines[i]:
            return sorted_lines[i - 2] + sorted_lines[i - 1] + sorted_lines[i]
    return -1


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        lines = list(map(int, inp.readline().strip().split()))
        print(solve(lines), file=outp)


if __name__ == "__main__":
    main()
