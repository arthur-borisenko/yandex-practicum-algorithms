MIN_COUPON_PRICE = 500 + 1


def main():
    with open("input.txt") as inp, open("output.txt", "w") as out:
        n = int(inp.readline())
        days = []
        for day in range(n):
            days.append(int(inp.readline()))
        usages = [[False for _ in range(n)] for _ in range(n)]
        next_day_variants = [(None, None) for _ in range(n)]

        for day in range(n - 1, -1, -1):
            current_day_variants = [(None, None) for _ in range(n)]
            for coupon in range(len(next_day_variants) - 1):
                if day + 1 == n:
                    usages[day][coupon] = coupon > 0
                    current_day_variants[coupon] = (
                        (0, coupon - 1) if coupon > 0 else (days[day], coupon)
                    )
                else:
                    if (
                        days[day] >= MIN_COUPON_PRICE
                        and coupon < len(next_day_variants) - 1
                    ):
                        sum_buy, coupon_buy = next_day_variants[coupon + 1]
                        if sum_buy is None:
                            sum_buy = 0
                            coupon_buy = coupon - day
                    else:
                        sum_buy, coupon_buy = next_day_variants[coupon]
                    sum_buy += days[day]
                    sum_skip, coupon_skip = next_day_variants[coupon - 1]
                    if sum_skip is not None and sum_skip < sum_buy:
                        sum_best, coupon_best = sum_skip, coupon_skip
                        usages[day][coupon] = True
                    else:
                        sum_best, coupon_best = sum_buy, coupon_buy
                    current_day_variants[coupon] = (sum_best, coupon_best)
            next_day_variants = current_day_variants
        best_usages = []
        coupon = 0
        for day in range(n):
            use_now = usages[day][coupon]
            if use_now:
                best_usages.append(day + 1)
                coupon -= 1
            elif days[day] >= MIN_COUPON_PRICE:
                coupon += 1
        dt = next_day_variants[0]
        if dt[0] is None:
            dt = [days[0], 0, []]
        print(dt[0], len(best_usages), file=out)
        print(*sorted(best_usages), file=out)


if __name__ == "__main__":
    main()
