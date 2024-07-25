def main():
    res = ""
    n = input()
    l1 = input().split()
    l2 = input().split()
    for i in range(2 * int(n)):
        if i % 2 == 0:
            res += l1[int(i / 2)] + " "
        else:
            res += l2[int((i - 1) / 2)] + " "
    print(res)


if __name__ == "__main__":
    main()
