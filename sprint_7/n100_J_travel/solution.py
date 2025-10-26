import math


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


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        l = list(map(int, inp.readline().split()))
        max_lengths = [0 for _ in range(n)]
        min_ends = [math.inf for _ in range(n + 1)]
        for i in range(n):
            ii = binary_nearest_search(min_ends, l[i])
            max_length = (ii if ii is not None else 0) + 1
            max_lengths[i] = max_length
            min_ends[max_length - 1] = min(min_ends[max_length], l[i])

        max_length = 0
        ii = 0
        for i, el in enumerate(max_lengths):
            if el > max_length:
                max_length = el
                ii = i
        prev_max_length = max_length + 1
        max_ascending_seq = []
        while ii >= 0:
            if max_lengths[ii] == prev_max_length - 1:
                max_ascending_seq.append(ii + 1)
                prev_max_length = max_lengths[ii]
            ii -= 1
        print(max_length, file=out)
        print(*reversed(max_ascending_seq), file=out)


if __name__ == "__main__":
    main()
