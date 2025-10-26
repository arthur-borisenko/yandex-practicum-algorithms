import math


def calc_max_chunks(input_seq: list[int]) -> int:
    """
    Calculates the maximum number of chunks the input array can be split which can be sorted separately, concatenated and result into sorted sequence.
    :param input_seq: source array
    :return: maximum number of chunks
    CPU - O(n)
    RAM - O(1)"""
    start_i = 0
    prev_max = min(input_seq) - 1
    current_min = math.inf
    current_max = -math.inf
    res = 0
    for i, el in enumerate(input_seq):
        current_min = min(current_min, el)
        current_max = max(current_max, el)
        if current_min <= prev_max + 1 and current_max - current_min == i - start_i:
            res += 1
            start_i = i + 1
            prev_max = current_max
            current_min = math.inf
            current_max = -math.inf
    return res


def main():
    """CPU - O(n + m)
    RAM - O(n + m)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        arr = list(map(int, inp.readline().split()))
        print(calc_max_chunks(arr), file=outp)


if __name__ == "__main__":
    main()
