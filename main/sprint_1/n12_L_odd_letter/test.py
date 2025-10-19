from utils import testUtil
import math



import main.sprint_1.n12_L_odd_letter.solution as task
import unittest

from utils import testUtil




def is_simple(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def checker(test_case, i: str, o):
    if i.splitlines()[0].count(o.strip()) != i.splitlines()[1].count(o.strip()):
        test_case.assertTrue(True, "OK")
    else:
        test_case.assertTrue(False, f"Output {o.strip()} is incorrect")


class TestCase(unittest.TestCase):
    def test_case1(self):
        inp = """abcd
abcde
"""
        value = testUtil.file_test(
            str(inp),
            task.main,
        )
        checker(self, inp, value)

    def test_case2(self):
        inp = """go
ogg
"""
        value = testUtil.file_test(
            str(inp),
            task.main,
        )
        checker(self, inp, value)

    def test_case3(self):
        inp = """xtkpx
xkctpx
"""
        value = testUtil.file_test(
            str(inp),
            task.main,
        )
        checker(self, inp, value)


if __name__ == "__main__":
    unittest.main()
