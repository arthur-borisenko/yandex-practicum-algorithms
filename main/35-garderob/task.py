def insertion_sort(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
    return array


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        items = list(map(int, inp.readline().strip().split()))
        print(*insertion_sort(items), file=outp)


if __name__ == "__main__":
    main()
