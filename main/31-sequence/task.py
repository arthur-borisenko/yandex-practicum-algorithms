def main():
    """CPU - O(n)
    RAM - O(n)"""
    with open("input.txt", "r") as inp, open("output.txt", "w") as outp:
        s = inp.readline().strip()
        t = inp.readline().strip()
        s_i = 0
        for el in t:
            if s_i < len(s) and s[s_i] == el:
                s_i += 1
        print(s_i == len(s), file=outp)


if __name__ == "__main__":
    main()
