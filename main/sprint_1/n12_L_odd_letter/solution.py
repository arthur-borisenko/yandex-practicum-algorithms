def main():
    """
    CPU - O(n)
    RAM - o(n)
    :return: Void
    """
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        line1 = inp.readline()
        line2 = inp.readline()
        letters1 = {}
        letters2 = {}
        for letter in line1:
            letters1[letter] = letters1.get(letter, 0) + 1
        for letter in line2:
            letters2[letter] = letters2.get(letter, 0) + 1
        for letter in letters2:
            if letters2[letter] != letters1.get(letter, 0):
                print(letter, file=outp)
                break


if __name__ == "__main__":
    main()
