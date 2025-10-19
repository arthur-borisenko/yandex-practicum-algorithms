from utils import testUtil
import main.sprint_2.n25_K_recursive_fibonacci_numbers.solution as task


import unittest

from utils import testUtil




class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3
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
            """0
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
            """6
""",
            task.main,
        )
        self.assertEqual(
            value,
            """13
""",
        )


if __name__ == "__main__":
    unittest.main()
