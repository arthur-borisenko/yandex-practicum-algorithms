from collections import defaultdict


def solve(a):
    if len(a) == 0:
        return 0
    prefixes = defaultdict(list)
    p = 0
    for i, el in enumerate(a):
        prefixes[p].append(i)
        p += -1 if int(el) == 0 else 1
    prefixes[p].append(len(a))
    max_dist = 0
    for key in prefixes.keys():
        if len(prefixes[key]) > 1:
            dist = prefixes[key][-1] - prefixes[key][0]
            if dist > max_dist:
                max_dist = dist
    return max_dist


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        a = list(map(int, inp.readline().split()))
        print(solve(a), file=out)


if __name__ == "__main__":
    main()
