def group_anagrams(strings):
    from collections import defaultdict

    groups = defaultdict(list)
    for idx, s in enumerate(strings, 1):
        key = "".join(sorted(s))
        groups[key].append(idx)
    return sorted([sorted(g) for g in groups.values()], key=lambda g: g[0])


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        strings = [inp.readline().strip() for _ in range(n)]
        result = group_anagrams(strings)
        for group in result:
            print(" ".join(map(str, group)), file=out)


if __name__ == "__main__":
    main()
