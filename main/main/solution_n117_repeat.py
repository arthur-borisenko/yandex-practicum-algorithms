def prefix_function(s):
    # Функция возвращает массив длины |s|
    n = len(s)
    prefix_func = [None] * n
    prefix_func[0] = 0
    for i in range(1, n):
        suffix_start_i = prefix_func[i - 1]
        while suffix_start_i > 0 and s[suffix_start_i] != s[i]:
            suffix_start_i = prefix_func[suffix_start_i - 1]
        if s[suffix_start_i] == s[i]:
            suffix_start_i += 1
        prefix_func[i] = suffix_start_i
    return prefix_func


def solve(s):
    ss = s.upper()
    n = len(ss)
    pp = prefix_function(ss)
    ccnt = n - pp[-1]
    v = n // ccnt if n % ccnt == 0 else 1
    return v


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as out:
        print(solve(inp.readline().strip()), file=out)


if __name__ == "__main__":
    main()
