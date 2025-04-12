from main.main import solution_n09_stepen_4 as task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """16
""",
            task.main,
        )
        self.assertEqual(
            value,
            """True
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """15
            """,
            task.main,
        )
        self.assertEqual(
            value,
            """False
""",
        )


if __name__ == "__main__":
    unittest.main()
