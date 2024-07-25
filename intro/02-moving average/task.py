def main():
    n = int(input())
    l = list(map(int, input().split()))
    k = int(input())
    res = []
    current_sum = sum(l[:k])
    res.append(current_sum / k)
    for i in range(n - k):
        current_first = l[i]
        current_last = l[i + k]
        current_sum -= current_first
        current_sum += current_last
        res.append(current_sum / k)
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
