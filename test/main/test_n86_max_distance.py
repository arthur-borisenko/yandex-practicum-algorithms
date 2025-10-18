from main.main import solution_n86_max_distance as task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5 4
2 1
4 5
4 3
3 2
2
""",
            task.main,
        )
        self.assertEqual(
            value,
            """3
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3 3
3 1
1 2
2 3
1
""",
            task.main,
        )
        self.assertEqual(
            value,
            """1
""",
        )

    def test_case3(self):
        value = testUtil.file_test(
            f"""6 8
6 1
1 3
5 1
3 5
3 4
6 5
5 2
6 2
4
""",
            task.main,
        )
        self.assertEqual(
            value,
            """3
""",
        )


if __name__ == "__main__":
    unittest.main()
