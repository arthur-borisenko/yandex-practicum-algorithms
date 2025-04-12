import math


def calc_max_chunks(input_seq: list[int]) -> int:
    """
    Calculates the maximum number of chunks the input array can be split, then sort all of them and get sorted array
    CPU - O(n)
    RAM - O(1)"""
    chunks_from_right = []
    min_from_right = math.inf
    for el in reversed(input_seq):
        min_from_right = min(min_from_right, el)
        chunks_from_right.append(min_from_right)

    max_from_left = -1
    chunks_from_left = []
    for el in input_seq:
        max_from_left = max(max_from_left, el)
        chunks_from_left.append(max_from_left)
    chunks = 1

    for i in range(len(chunks_from_left) - 1):
        min_from_right = chunks_from_right[-i - 2]
        max_from_left = chunks_from_left[i]
        if min_from_right >= max_from_left:
            chunks += 1
    return chunks


def main():
    """CPU - O(n + m)
    RAM - O(n + m)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        arr = list(map(int, inp.readline().split()))
        print(calc_max_chunks(arr), file=outp)


if __name__ == "__main__":
    main()
