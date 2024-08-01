import math

import task
import unittest

from utils import testUtil


def is_simple(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def checker(test_case, i, o):
    res = 1
    for val in o.split():
        if not is_simple(int(val)):
            raise AssertionError("factorization must return list of simple numbers")
        res *= int(val)
    test_case.assertEqual(i, res)


class TestCase(unittest.TestCase):
    def test_case1(self):
        inp = 464458159
        value = testUtil.file_test(
            str(inp),
            task.main,
        )
        checker(self, inp, value)

    def test_case2(self):
        inp = 13
        value = testUtil.file_test(
            str(inp),
            task.main,
        )
        checker(self, inp, value)

    def test_case3(self):
        inp = 8
        value = testUtil.file_test(
            str(inp),
            task.main,
        )
        checker(self, inp, value)


if __name__ == "__main__":
    unittest.main()
