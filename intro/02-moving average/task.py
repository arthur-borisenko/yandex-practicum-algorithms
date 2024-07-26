def main():
    n = int(input())  # O(1)
    l = list(map(int, input().split()))  # O(1)
    k = int(input())  # O(1)
    res = []  # O(1)
    current_sum = sum(l[:k])  # O(n)
    res.append(current_sum / k)  # O(1)
    for i in range(n - k):  # O(n)
        current_first = l[i]  # O(1)
        current_last = l[i + k]  # O(1)
        current_sum -= current_first  # O(1)
        current_sum += current_last  # O(1)
        res.append(current_sum / k)  # O(1)
    print(" ".join(map(str, res)))  # O(n)


if __name__ == "__main__":
    main()
