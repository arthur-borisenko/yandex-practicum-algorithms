from main.main import solution_n36_big_number as task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3
15 56 2
""",
            task.main,
        )
        self.assertEqual(
            value,
            """56215
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3
1 783 2
""",
            task.main,
        )
        self.assertEqual(
            value,
            """78321
""",
        )

    def test_case3(self):
        value = testUtil.file_test(
            """5
2 4 5 2 10
""",
            task.main,
        )
        self.assertEqual(
            value,
            """542210
""",
        )


if __name__ == "__main__":
    unittest.main()
