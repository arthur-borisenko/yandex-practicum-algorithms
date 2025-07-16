def cals_max_substring_with_unique_symbols_len(s):
    ss = set()
    ml = 0
    left = 0
    for i in range(len(s)):
        el = s[i]
        if el in ss:
            if len(ss) > ml:
                ml = len(ss)
            while el in ss:
                ss.remove(s[left])
                left += 1
        ss.add(el)
    if len(ss) > ml:
        ml = len(ss)
    return ml


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        print(
            cals_max_substring_with_unique_symbols_len(inp.readline().strip()), file=out
        )


if __name__ == "__main__":
    main()
