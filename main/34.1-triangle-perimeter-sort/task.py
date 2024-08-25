import array


def count_sort(arr, reverse=False) -> None:
    """CPU - O(n+max(arr))
    RAM - O(max(arr))
    sorts input array of positive integers
    :param arr: array of non-negative integers to sort
    :param reverse: if False(default), sort in ascending order, if True, sort in descending order
    """
    counts = array.array("q", [0] * (max(arr) + 1))
    for el in arr:
        counts[el] = counts[el] + 1
    index = 0
    for i in range(min(arr), max(arr) + 1):
        for j in range(counts[i]):
            arr[index if not reverse else -(index + 1)] = i
            index += 1


def solve(lines):
    """CPU - O(n+max(lines))
    RAM - O(max(lines))"""
    count_sort(lines, reverse=True)
    for i in range(2, len(lines)):
        if lines[i - 2] < lines[i - 1] + lines[i]:
            return lines[i - 2] + lines[i - 1] + lines[i]
    return -1


def main():
    """CPU - O(n+max(lines))
    RAM - O(n+max(lines))"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        lines = list(map(int, inp.readline().strip().split()))
        print(solve(lines), file=outp)


if __name__ == "__main__":
    main()
