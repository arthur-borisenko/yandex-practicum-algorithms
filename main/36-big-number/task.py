def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = key


def main():
    """CPU - O(n)
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        inp_data = list(
            map(lambda x: int, filter(lambda x: x.isdigit(), inp.readline().split()))
        )
        insertion_sort(inp_data)


if __name__ == "__main__":
    main()
