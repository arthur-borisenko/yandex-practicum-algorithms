def strange_comparison(a, b, changed=False):
    if abs(len(a) - len(b)) > 2:
        return False
    i = 0
    while i < max(len(a), len(b)):
        if i >= min(len(a), len(b)):
            if not changed:
                changed = True
            else:
                return False
        else:
            if a[i] != b[i]:
                if not changed:
                    return (
                        strange_comparison(a[i + 1 :], b[i + 1 :], True)
                        or strange_comparison(a[i + 1 :], b[i:], True)
                        or strange_comparison(a[i:], b[i + 1 :], True)
                    )
                else:
                    return False
        i += 1
    return True


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        x = inp.readline().strip()
        y = inp.readline().strip()
        print("OK" if strange_comparison(x, y) else "FAIL", file=out)


if __name__ == "__main__":
    main()
