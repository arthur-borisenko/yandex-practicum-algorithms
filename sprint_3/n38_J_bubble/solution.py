def bubble_sort_print_all_steps(arr, print_file, key=lambda x: x, reverse=False):
    """CPU - O(n**2)
    RAM - O(1)"""
    need_print = True
    new_arr = list(arr)
    for i in range(len(new_arr) - 1):
        print_iter = False
        for j in range(len(new_arr) - i - 1):
            if key(new_arr[j]) > key(new_arr[j + 1]):
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
                print_iter = True
        if print_iter:
            print(*new_arr, file=print_file)
            need_print = False
    if need_print:
        print(*new_arr, file=print_file)
    return list(reversed(new_arr)) if reverse else new_arr


def main():
    """CPU - O(n**2)
    RAM - O(1)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        arr = map(int, inp.readline().split())
        bubble_sort_print_all_steps(arr, outp)


if __name__ == "__main__":
    main()
