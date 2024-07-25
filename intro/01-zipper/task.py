def main():
    res = ""
    n = input()
    l1 = input().split()
    l2 = input().split()
    for i in range(int(n)):
        res += l1[i] + " "
        res += l2[i] + " "
    print(res)


if __name__ == "__main__":
    main()
