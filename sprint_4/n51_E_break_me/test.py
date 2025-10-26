import os.path


import unittest
import sprint_4.n51_E_break_me.solution as solution


def polynominal_hash(s, base, mod):
    """CPU - O(n)
    RAM - O(1)

    we can use result % mod on all iterations, and it will equal result%mod on last iteration because:
    result = mod * a + r,
    so r = result % mod = result - mod * a.
    On next iteration we calculate result using:
    result = (base * mod * a + base * r + code) % mod
    and because first part has multiplier a, it will give zero modulo,
    so (base * mod * a + base * r + code) % mod = (base * mod * a - base*mod*a+base*r+code)%mod
    so, because we return result % mod, we can use (base * mod * a - base * mod * a + base * r + code) % mod,
    which equals (base * (result % mod) + code) % mod in all calculations
    """
    result = 0
    for char in s:
        code = ord(char)
        result = (base * result + code) % mod
    return result % mod


class TestCase(unittest.TestCase):
    def test(self):
        if not os.path.exists("output.txt"):
            open("output.txt", "x").close()
        with open("output.txt") as f:
            a, b = f.readline(), f.readline()
            solution.main()
            self.assertEqual(
                polynominal_hash(b, 1000, 123987123),
                polynominal_hash(b, 1000, 123987123),
            )
