from main.intro.n03_two_chips import task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """6
-1 -1 -9 -7 3 -6
2""",
            task.main,
        )
        self.assertEqual(
            value.strip(),
            """-1 3""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """8
6 2 8 -3 1 1 6 10
100""",
            task.main,
        )
        self.assertEqual(value.strip(), """None""")


if __name__ == "__main__":
    unittest.main()
