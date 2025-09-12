def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        m = int(inp.readline())
        n = int(inp.readline())
        nominals = list(map(int, inp.readline().split()))
        dp = [-1 for _ in range(m + 1)]
        dp[0] = 0
        for sum_needed in range(1, m + 1):
            min_banknotes_cnt = -1
            for nominal in nominals:
                if sum_needed < nominal or dp[sum_needed - nominal] == -1:
                    continue
                current_banknotes_cnt = dp[sum_needed - nominal] + 1
                if min_banknotes_cnt == -1 or current_banknotes_cnt < min_banknotes_cnt:
                    min_banknotes_cnt = current_banknotes_cnt
            dp[sum_needed] = min_banknotes_cnt
        print(dp[-1], file=out)


if __name__ == "__main__":
    main()
