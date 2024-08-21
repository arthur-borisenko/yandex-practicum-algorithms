def bubble_sort(
    arr, key=lambda x: x, less_comparator=lambda x, y: x < y, reverse=False
):
    new_arr = list(map(key, arr))
    for i in range(len(new_arr) - 1):
        for j in range(len(new_arr) - i - 1):
            if less_comparator(new_arr[j], new_arr[j + 1]):
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
    return list(reversed(new_arr)) if reverse else new_arr


def main():
    """CPU - O(n**2)
    RAM - O(1)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        inp_data = inp.readline().split()
        print(
            "".join(bubble_sort(inp_data)),
            file=outp,
        )


if __name__ == "__main__":
    main()
