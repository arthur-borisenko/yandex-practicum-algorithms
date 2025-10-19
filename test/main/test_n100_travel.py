import unittest
import main.main.solution_n100_travel as task
from test.utils import testUtil


class TestCase(unittest.TestCase):
    def check(self, il, val, el):
        self.assertGreaterEqual(len(val.splitlines()), 2)
        l, d = val.splitlines()[:2]
        latest = -1
        self.assertEqual(int(l), len(d.split()))
        self.assertEqual(int(l), el)
        for el in d.split():
            self.assertGreater(il[int(el) - 1], latest)
            latest = il[int(el) - 1]
        return True

    def test_case1(self):
        value = testUtil.file_test(
            """5
4 2 9 1 13

""".rstrip(),
            task.main,
        )
        self.check([4, 2, 9, 1, 13], value, 3)

    def test_case2(self):
        value = testUtil.file_test(
            """6
1 2 4 8 16 32

""".rstrip(),
            task.main,
        )
        self.check([1, 2, 4, 8, 16, 32], value, 6)

    def test_case3(self):
        value = testUtil.file_test(
            """7
3 6 10 1 9 3 10
""".rstrip(),
            task.main,
        )
        self.check([3, 6, 10, 1, 9, 3, 10], value, 4)

    def test_case4(self):
        value = testUtil.file_test(
            """7
10 9 10 10 1 6 10
""",
            task.main,
        )
        self.check([10, 9, 10, 10, 1, 6, 10], value, 3)


if __name__ == "__main__":
    unittest.main()
