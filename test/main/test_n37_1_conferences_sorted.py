from main.main import solution_n37_1_conferences_sorted as task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """7
1 2 3 1 2 3 4 4 4
4
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """4 1 2 3
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """6
1 1 1 2 2 3
1
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """1
""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """6
8 8 8 3 3 3 3 4
3
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3 8 4
""".rstrip(),
        )

    def test_case4(self):
        value = testUtil.file_test(
            """5
2 2 2 2 2
2
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2
""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
