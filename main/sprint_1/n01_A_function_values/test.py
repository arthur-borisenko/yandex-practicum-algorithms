from utils import testUtil
import main.sprint_1.n01_A_function_values.solution as task


import unittest

from utils import testUtil


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
