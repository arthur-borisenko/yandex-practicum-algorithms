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
            res.append((res[-1] * base + ord(el)) % mod)
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
a_hashes = PrefixHasher(a, 10**9 + 7, 2**16 - 1)
b_hashes = PrefixHasher(b, 10**9 + 7, 2**16 - 1)


def idk(a, b, a_ph, b_ph, le):
    b_hs = set()
    for i in range(len(b)):
        b_hs.add(b_ph[i : i + le])
    for i in range(len(a)):
        if a_ph[i : i + le] in b_hs:
            return True
    return False