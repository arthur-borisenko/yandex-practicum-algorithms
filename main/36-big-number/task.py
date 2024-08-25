import functools

def cmp(x, y):
    ,
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
