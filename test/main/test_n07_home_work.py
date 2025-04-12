from main.main import solution_n07_home_work as task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5
""",
            task.main,
        )
        self.assertEqual(
            value,
            """101
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """14
            """,
            task.main,
        )
        self.assertEqual(
            value,
            """1110
""",
        )


if __name__ == "__main__":
    unittest.main()
