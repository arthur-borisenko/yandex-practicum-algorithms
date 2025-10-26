import array


import math
import random

import sprint_1.n11_K_list_form.solution as task
import unittest

from utils import testUtil


def array_iterator(arr):
    i = 0
    while i < len(arr):
        yield arr[i]
        i += 1


def is_simple(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def checker(test_case, i, o):
    l, n, k = i.splitlines()
    int_n = int("".join(n.split()))
    int_k = int(k)
    int_o = int("".join(o.split()))
    test_case.assertEqual(int_n + int_k, int_o)


def get_random_ints_array(n, min_val=0, max_val=9):
    res = array.array("i", (0,) * n)
    for i in range(n):
        res[i] = random.randint(min_val, max_val)
    return res


class TestCase(unittest.TestCase):
    def test_case1(self):
        inp = """4
1 2 0 0
34
"""
        value = testUtil.file_test(
            str(inp),
            task.main,
        )
        checker(self, inp, value)

    def test_case2(self):
        inp = """2
9 5
17
"""
        value = testUtil.file_test(
            str(inp),
            task.main,
        )
        checker(self, inp, value)

    def test_case3(self):
        inp = f"""{1000}
        {" ".join(map(str,array_iterator(get_random_ints_array(1000))))}
        10000"""
        value = testUtil.file_test(
            str(inp),
            task.main,
        )
        checker(self, inp, value)


if __name__ == "__main__":
    unittest.main()
