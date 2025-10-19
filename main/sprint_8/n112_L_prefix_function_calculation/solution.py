def prefix_function(s):
    # Функция возвращает массив длины |s|
    n = len(s)
    prefix_func = [None] * n
    prefix_func[0] = 0
    for i in range(1, n):
        k = prefix_func[i - 1]
        while k > 0 and s[k] != s[i]:
            k = prefix_func[k - 1]
        if s[k] == s[i]:
            k += 1
        prefix_func[i] = k
    return prefix_func


def main():
    with open("input.txt", encoding="utf-8") as inp, open(
        "output.txt", "w", encoding="utf-8"
    ) as out:
        print(*prefix_function(inp.readline().strip()), file=out)


if __name__ == "__main__":
    main()
