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
