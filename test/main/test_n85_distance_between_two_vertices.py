from main.main import solution_n85_distance_between_vertices as task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5 5
2 4
3 5
2 1
2 3
4 5
1 5
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
            """4 3
2 3
4 3
2 4
1 3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """-1
""",
        )

    def test_case3(self):
        value = testUtil.file_test(
            f"""2 1
2 1
1 1
""",
            task.main,
        )
        self.assertEqual(
            value,
            """0
""",
        )


if __name__ == "__main__":
    unittest.main()
