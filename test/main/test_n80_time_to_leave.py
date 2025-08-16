from main.main import solution_n80_time_to_leave as task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """6 8
2 6
1 6
3 1
2 5
4 3
3 2
1 2
1 4
""",
            task.main,
        )
        self.assertEqual(
            value,
            """0 11
1 6
8 9
7 10
2 3
4 5
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3 2
1 2
2 3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """0 5
1 4
2 3
""",
        )


if __name__ == "__main__":
    unittest.main()
