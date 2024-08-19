import task
import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """4
6 3 3 2""",
            task.main,
        )
        self.assertEqual(
            value,
            """8
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """6
5 3 7 2 8 3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """20
""",
        )


if __name__ == "__main__":
    unittest.main()
