import unittest
from main.main import solution_n43_partial_sort as task
from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """4
0 1 3 2
""",
            task.main,
        )
        self.assertEqual(
            value.strip(),
            """3
""".strip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """8
3 6 7 4 1 5 0 2
""",
            task.main,
        )
        self.assertEqual(
            value.strip(),
            """1
""".strip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """5
1 0 2 3 4
""",
            task.main,
        )
        self.assertEqual(
            value.strip(),
            """4
""".strip(),
        )


if __name__ == "__main__":
    unittest.main()
