from main.main import solution_n01_function_values as task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """-8 -5 -2 7
""",
            task.main,
        )
        self.assertEqual(
            value.strip(),
            """-183""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """8 2 9 -10
""",
            task.main,
        )
        self.assertEqual(value.strip(), """40""")


if __name__ == "__main__":
    unittest.main()
