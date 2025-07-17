import unittest
from main.main import solution_n48_competition as task
from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """2
0 1
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3
0 1 0
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2
""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """10
0 0 1 0 1 1 1 0 0 0
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """8
""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
