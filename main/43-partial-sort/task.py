def solve(arr):
    """CPU - O(n)
    RAM - O(1)"""
    max_from_left = -1
    mins_from_right = []
    min_from_right = len(arr) - 1
    for i, el in enumerate(reversed(arr)):
        if el < min_from_right:
            min_from_right = el
        mins_from_right.append(min_from_right)
    max_from_left = -1
    maxes_from_left = []
    for i, el in enumerate(arr):
        if el > max_from_left:
            max_from_left = el
        maxes_from_left.append(max_from_left)
    res = 1
    for i in range(len(maxes_from_left) - 1):
        min_from_right = mins_from_right[-i - 2]
        max_from_left = maxes_from_left[i]
        if min_from_right >= max_from_left:
            res += 1
    return res


def main():
    """CPU - O(n + m)
    RAM - O(n + m)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        arr = list(map(int, inp.readline().split()))
        print(solve(arr), file=outp)


if __name__ == "__main__":
    main()
