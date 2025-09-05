def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        l = list(map(int, inp.readline().split()))
        r = []
        for si in range(len(l)):
            rt = []
            mx = l[si]
            for i in range(si, len(l)):
                if l[i] >= mx:
                    rt.append(i + 1)
                    mx = l[i]
            r = max(r, rt, key=len)
        print(len(r), file=out)
        print(*r, file=out)


if __name__ == "__main__":
    main()
