def find_closing_bracket(s, i):
    cnt = 0
    for ii in range(i, len(s)):
        ss = s[ii]
        if ss == "[" and ii > 0:
            cnt += 1
        elif ss == "]":
            cnt -= 1
        if cnt == 0:
            return ii


def decompress(s):
    res = []
    i = 0
    while i < len(s):
        if s[i] == "[" and i > 0 and s[i - 1].isdigit():
            ni = find_closing_bracket(s, i)
            cnt = int(s[i - 1])
            res.append(decompress(s[i + 1 : ni]) * cnt)
            i = ni
        elif (not s[i].isdigit()) or (i + 1 >= len(s)) or s[i + 1] != "[":
            res.append(s[i])
        i += 1
    return "".join(res)


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        ss = []
        for i in range(n):
            ss.append(decompress(inp.readline()))
        p = ss.pop()
        while ss:
            s = ss.pop()
            if s[0] != p[0]:
                p = []
                break
            i = 0
            for i in range(len(p)):
                if i + 1 >= len(s) or i + 1 >= len(p) or p[i + 1] != s[i + 1]:
                    break
            p = p[: i + 1]
        print("".join(p), file=out)


if __name__ == "__main__":
    main()
