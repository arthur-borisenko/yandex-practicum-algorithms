from collections import defaultdict


class PrefixHasher:
    def __init__(self, seq, base, mod):
        self.base = base
        self.mod = mod
        self.s = seq
        self.powers, self.prefixes = self.precompute(seq, base, mod)

    @staticmethod
    def prefix_hashes(s, base, mod):
        res = [0]
        for el in s:
            res.append((res[-1] * base + el) % mod)
        return res

    @staticmethod
    def precompute_powers(base, exp, mod):
        powers = [1]
        for _ in range(exp):
            powers.append((powers[-1] * base) % mod)
        return powers

    def precompute(self, s, base, mod):
        powers = self.precompute_powers(base, len(s), mod)
        prefixes = self.prefix_hashes(s, base, mod)
        return powers, prefixes

    def subhash(self, left, right):
        return (
            self.prefixes[right + 1]
            - self.prefixes[left] * self.powers[(right - left + 1)]
            + self.mod
        ) % self.mod

    def __getitem__(self, item):
        if isinstance(item, slice):
            left, right = item.start, item.stop
            return self.subhash(left, right)
        raise TypeError


def parse_input(inp):
    n = int(inp.readline())
    a = list(map(int, inp.readline().split()))
    m = int(inp.readline())
    b = list(map(int, inp.readline().split()))
    return n, m, a, b


def has_common_subarray_of_length(aa, bb, a_ph, b_ph, a_ph2, b_ph2, le):
    b_hs = set()
    b_hs2 = set()
    for i in range(len(bb) - le):
        b_hs.add(b_ph[i : i + le])
    for i in range(len(bb) - le):
        b_hs2.add(b_ph2[i : i + le])
    for i in range(len(aa) - le):
        if a_ph[i : i + le] in b_hs and a_ph2[i : i + le] in b_hs2:
            return True
    return False


def precompute_prefix_hashes(a, b):
    a_hashes = PrefixHasher(a, 10**9 + 7, 1234567891)
    b_hashes = PrefixHasher(b, 10**9 + 7, 1234567891)
    a_hashes2 = PrefixHasher(a, 10**9 + 9, 2**31 - 1)
    b_hashes2 = PrefixHasher(b, 10**9 + 9, 2**31 - 1)
    return a_hashes, b_hashes, a_hashes2, b_hashes2


def search(a, b):
    a_hashes, b_hashes, a_hashes2, b_hashes2 = precompute_prefix_hashes(a, b)
    left = 0
    right = len(b) - 1
    while left <= right:
        mid = (left + right) // 2
        if has_common_subarray_of_length(
            a, b, a_hashes, b_hashes, a_hashes2, b_hashes2, mid
        ):
            left = mid + 1
        else:
            right = mid - 1
    return left


def main():
    with open("input.txt", "r") as inp, open("output.txt", "w") as out:
        n, m, a, b = parse_input(inp)
        print(search(a, b), file=out)


if __name__ == "__main__":
    main()
