from main.main import solution_n22_bracket_sequence as task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """(){[()]}
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
            """[{]}
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
