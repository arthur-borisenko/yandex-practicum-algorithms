def solution(n):
    """CPU - O(n^2)
    RAM - O(n)"""
    solutions = {0: 1, 1: 1}
    variants = 0
    for i in range(1, length + 1):
        variants = 0
        for j in range(i):
            variants += solutions[j] * solutions[i - j - 1]
        solutions[i] = variants
    return variants


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        x = int(inp.readline())
        print(solution(x), file=out)
