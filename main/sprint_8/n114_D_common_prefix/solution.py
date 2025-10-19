def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = int(inp.readline().strip())
        ss = []
        for i in range(n):
            ss.append(inp.readline().strip())
        p = ss.pop()
        while ss:
            s = ss.pop()
            if s[0] != p[0]:
                p = []
                break
            for i in range(len(p)):
                if i + 1 >= len(s) or i + 1 >= len(p) or p[i + 1] != s[i + 1]:
                    break
            p = p[: i + 1]
        print(len(p), file=out)


if __name__ == "__main__":
    main()
