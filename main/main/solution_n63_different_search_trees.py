def solution(data):
    if len(data) == 1:
        return 1
    if len(data) == 0:
        return 1
    variants = 0
    for i in range(len(data)):
        left_data = data[:i]
        right_data = data[(i + 1) :]
        variants += solution(left_data) * solution(right_data)
        pass
    return variants


def main():
    with open("input.txt") as inp, open(
        "output.txt", "w"
    ) as out:
        print(solution(list(range(int(inp.readline())))), file=out)
