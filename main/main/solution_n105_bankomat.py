from collections import defaultdict

ddd = defaultdict(dict)


def aaaa(dt, tt, mt):
    mt1 = mt
    mt -= tt if tt is not None else 0
    if mt < 0:
        return 0
    if mt == 0:
        return 1
    r = 0
    for d in dt:
        if tt is not None and d < tt:
            continue
        res = aaaa(dt, d, mt)
        r += res
    ddd[mt1][tt] = r
    return r


def main():
    m = int(input())
    n = int(input())
    l = list(map(int, input().split()))
    ff = aaaa(l, None, m)
    print(ff + 1)


if __name__ == "__main__":
    main()
