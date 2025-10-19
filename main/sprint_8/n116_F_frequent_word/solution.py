def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = int(inp.readline().strip())
        ss = []
        for i in range(n):
            ss.append(inp.readline().strip())
        cnts = {}
        for s in ss:
            cnts[s] = cnts.get(s, 0) + 1
        frequentest_word = None
        for s, cnt in cnts.items():
            if frequentest_word is None or cnt > cnts[frequentest_word]:
                frequentest_word = s
            if frequentest_word is not None and cnt == cnts[frequentest_word]:
                frequentest_word = min(s, frequentest_word)
        print(frequentest_word, file=out)


if __name__ == "__main__":
    main()
