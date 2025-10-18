import sys


def pi(inp):
    r = []
    n = int(inp.readline())
    for i in range(n):
        a, b = inp.readline().split()
        aa = a.split(".")
        bb = b.split(".")
        if len(aa) == 1:
            aaa = int(aa[0]) * 60
        else:
            aaa = int(aa[0]) * 60 + int(aa[1])
        if len(bb) == 1:
            bbb = int(bb[0]) * 60
        else:
            bbb = int(bb[0]) * 60 + int(bb[1])
        r.append((aaa, bbb))
    return r


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        rr = pi(inp)
        rr1 = sorted(rr, key=lambda x: (x[1], x[0]))
        rrr = []
        t = 0
        for el in rr1:
            if el[0] >= t:
                t = el[1]
                rrr.append(list(map(lambda x: f"{x // 60}.{x % 60}", el)))
        print(len(rrr), file=out)
        for v in rrr:
            print(*v, file=out)


if __name__ == "__main__":
    main()
