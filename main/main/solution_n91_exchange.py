def main():
    with open("input.txt","r") as inp, open("output.txt","w") as out:
        n = int(inp.readline())
        ps = list(map(int, inp.readline().split()))
        bp = 0
        sp = 0
        pp = None
        for i, el in enumerate(ps):
            if i + 1 < len(ps):
                ne = ps[i + 1]
                if el < ne:
                    if pp is None:
                        bp += el
                        pp = el
                elif el > ne:
                    if pp is not None:
                        sp += el
                        pp = None
            else:
                if pp is not None:
                    sp += el
                    pp = None
        print(sp - bp, file=out)

if __name__ == '__main__':
    main()
