from utils import testUtil
import main.sprint_3.n30_B_1_combinations_recursion.solution as task


import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """92
""",
            task.main,
        )
        self.assertEqual(
            value,
            """wa wb wc xa xb xc ya yb yc za zb zc
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """23
""",
            task.main,
        )
        self.assertEqual(
            value,
            """ad ae af bd be bf cd ce cf
""",
        )

    def test_case3(self):
        value = testUtil.file_test(
            """2
""",
            task.main,
        )
        self.assertEqual(
            value,
            """a b c
""",
        )


if __name__ == "__main__":
    unittest.main()
