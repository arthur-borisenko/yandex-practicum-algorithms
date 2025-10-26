import sprint_1.n05_E_longest_word.solution as task


import unittest
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """19
i love segment tree
""",
            task.main,
        )
        self.assertEqual(
            value,
            """segment
7
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """21
frog jumps from river
""",
            task.main,
        )
        self.assertEqual(
            value,
            """jumps
5
""",
        )


if __name__ == "__main__":
    unittest.main()
