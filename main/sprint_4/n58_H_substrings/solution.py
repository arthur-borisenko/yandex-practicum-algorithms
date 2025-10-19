def cals_max_substring_with_unique_symbols_len(s: str) -> int:
    """CPU - O(n)
    RAM - O(n)"""
    sub_s = set()
    max_length = 0
    left = 0
    for s_char in s:
        if s_char in sub_s:
            if len(sub_s) > max_length:
                max_length = len(sub_s)
            while s_char in sub_s:
                sub_s.remove(s_char)
                left += 1
        sub_s.add(s_char)
    if len(sub_s) > max_length:
        max_length = len(sub_s)
    return max_length


def main():
    """CPU - O(n)
    RAM - O(n)"""
    with open("input.txt") as inp, open("output.txt", "w") as out:
        print(
            cals_max_substring_with_unique_symbols_len(inp.readline().strip()), file=out
        )


if __name__ == "__main__":
    main()
