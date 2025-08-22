from main.main import solution_n90_connectivity_components as task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """6 3
1 2
6 5
2 3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """3
1 2 3
4
5 6
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """2 0
""",
            task.main,
        )
        self.assertEqual(
            value,
            """2
1
2
""",
        )

    def test_case3(self):
        value = testUtil.file_test(
            f"""4 3
2 3
2 1
4 3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """1
1 2 3 4
""",
        )


if __name__ == "__main__":
    unittest.main()
