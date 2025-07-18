from collections import defaultdict


class PrefixHasher:
    def __init__(self, seq, base, mod):
        self.base = base
        self.mod = mod
        self.s = seq
        self.powers, self.prefixes = self.precompute(seq, base, mod)

    def prefix_hashes(self, s, base, mod):
        res = [0]
        for el in s:
            res.append((res[-1] * base + el) % mod)
        return res

    def precompute_powers(self, base, exp, mod):
        powers = [1]
        for _ in range(exp):
            powers.append((powers[-1] * base) % mod)
        return powers

    def precompute(self, s, base, mod):
        powers = self.precompute_powers(base, len(s), mod)
        prefixes = self.prefix_hashes(s, base, mod)
        return powers, prefixes

    def subhash(self, mod, left, right, powers, prefixes):
        return (
            prefixes[right + 1] - prefixes[left] * powers[(right - left + 1)] + mod
        ) % mod

    def __getitem__(self, item):
        if isinstance(item, slice):
            left, right = item.start, item.stop
            return self.subhash(self.mod, left, right, self.powers, self.prefixes)
        raise TypeError


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a_hashes = PrefixHasher(a, 10**9 + 7, 1234567891)
b_hashes = PrefixHasher(b, 10**9 + 7, 1234567891)
a_hashes2 = PrefixHasher(a, 10**9 + 9, 2**31 - 1)
b_hashes2 = PrefixHasher(b, 10**9 + 9, 2**31 - 1)


def idk(aa, bb, a_ph, b_ph, a_ph2, b_ph2, le):
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


def search(a, b):
    left = 0
    right = len(b) - 1
    while left <= right:
        mid = (left + right) // 2
        if idk(a, b, a_hashes, b_hashes, a_hashes2, b_hashes2, mid):
            left = mid + 1
        else:
            right = mid - 1
    return left


print(search(a, b))
