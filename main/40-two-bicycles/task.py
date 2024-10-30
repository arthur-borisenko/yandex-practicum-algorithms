def binary_nearest_search(seq, target, key=lambda x: x):
    start = 0
    end = len(seq) - 1
    while start <= end:
        mid = (start + end) // 2
        if key(seq[mid]) < target:
            start = mid + 1
        elif mid != 0 and key(seq[mid - 1]) >= target:
            end = mid - 1
        else:
            return mid
    return -2


def main():
    """CPU - O(log(n))
    RAM - O(1)"""
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        arr = list(map(int, inp.readline().split()))
        s = int(inp.readline())
        print(
            binary_nearest_search(arr, s) + 1,
            binary_nearest_search(arr, s * 2) + 1,
            file=outp,
        )


if __name__ == "__main__":
    main()
