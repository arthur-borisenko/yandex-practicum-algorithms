from typing import Iterable


def main():
    """CPU - O(n log(n))
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        n = int(inp.readline())
        lns = inp.readlines()
        parsed_lines: Iterable[list[int]] = map(
            lambda l: list(map(int, l.split())), lns
        )
        print_output(solve(parsed_lines), file=outp)


def print_output(out, file):
    for line in out:
        print(*line, file=file)


def solve(lines: Iterable):
    """CPU - O(n log(n))
    RAM - O(n)"""
    max_end = float("-inf")
    max_end_pair = -1
    res = []
    res_pair_i = 0
    sorted_lns = sorted(lines)
    for line in sorted_lns:
        if line[0] > max_end:
            res.append(line)
            max_end = line[1]
            max_end_pair = res_pair_i
        else:
            if line[1] > max_end:
                res[max_end_pair][1] = line[1]
                max_end = line[1]
        res_pair_i += 1
    return res


if __name__ == "__main__":
    main()
