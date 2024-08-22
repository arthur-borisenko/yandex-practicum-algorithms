def bubble_sort_k_biggest_items(arr, k, key=lambda x: x):
    new_arr = list(arr)
    for i in range(k):
        for j in range(len(new_arr) - i - 1):
            if key(new_arr[j]) > key(new_arr[j + 1]):
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
        pass
    new_arr = new_arr[-k:]
    return list(reversed(new_arr))


def _count(arr):
    """CPU - O(n)
    RAM - O(n)"""
    counts = {}
    for el in arr:
        counts[el] = counts.get(el, 0) + 1
    return counts


def main():
    """CPU - O(nk)
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        arr = map(int, inp.readline().split())
        k = int(inp.readline())
        print(
            " ".join(
                map(
                    lambda x: str(x[0]),
                    bubble_sort_k_biggest_items(
                        _count(arr).items(), k, key=lambda x: (x[1], -x[0])
                    ),
                )
            ),
            file=outp,
        )


if __name__ == "__main__":
    main()
