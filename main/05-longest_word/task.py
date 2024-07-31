def main():
    """
    cpu - O(n)
    ram - o(n)
    n - words in input.txt
    :return: Void
    """
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        l = int(inp.readline())
        words = list(inp.readline().split())
        res = None
        for word in words:
            if not res or len(word) > len(res):
                res=word
        print(res, file=outp)
        print(len(res), file=outp)


if __name__ == "__main__":
    main()
