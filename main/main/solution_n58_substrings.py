def cals_max_substring_with_unique_symbols_len(string: str) -> int:
    """CPU - O(n)
    RAM - O(n)"""
    current_symbols = set()
    max_length = 0
    left = 0
    for i, symbol in enumerate(string):
        if symbol in current_symbols:
            if len(current_symbols) > max_length:
                max_length = len(current_symbols)
            while symbol in current_symbols:
                current_symbols.remove(string[left])
                left += 1
        current_symbols.add(symbol)
    if len(current_symbols) > max_length:
        max_length = len(current_symbols)
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
