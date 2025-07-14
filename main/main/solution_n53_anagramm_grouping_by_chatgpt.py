def group_anagrams(strings):
    from collections import defaultdict

    groups = defaultdict(list)
    for idx, s in enumerate(strings, 1):
        key = "".join(sorted(s))
        groups[key].append(idx)
    return sorted([sorted(g) for g in groups.values()], key=lambda g: g[0])


def main():
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    result = group_anagrams(strings)
    for group in result:
        print(" ".join(map(str, group)))


if __name__ == "__main__":
    main()
