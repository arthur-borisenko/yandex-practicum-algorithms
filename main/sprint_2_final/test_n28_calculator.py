import unittest
from main.sprint_2_final import solution_n28_calculator as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """2 1 + 3 *
""",
            task.main,
        )
        self.assertEqual(
            value,
            """9
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """7 2 + 4 * 2 +
""",
            task.main,
        )
        self.assertEqual(
            value,
            """38
""",
        )


if __name__ == "__main__":
    unittest.main()
