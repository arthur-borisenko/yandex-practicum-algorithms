from main.intro.n04_two_chips_efficent import task_1
from main.intro.n04_two_chips_efficent import task_2
import unittest

from test.utils import testUtil


class TestCaseTask1(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """6
-1 -1 -9 -7 3 -6
2""",
            task_1.main,
        )
        self.assertEqual(
            set(value.strip().split()),
            {"-1", "3"},
        )

    def test_case2(self):
        value = testUtil.file_test(
            """8
6 2 8 -3 1 1 6 10
100""",
            task_1.main,
        )
        self.assertEqual(
            set(value.strip().split()),
            {"None"},
        )


if __name__ == "__main__":
    unittest.main()


class TestCaseTask2(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """6
-1 -1 -9 -7 3 -6
2""",
            task_2.main,
        )
        self.assertEqual(
            set(value.strip().split()),
            {"-1", "3"},
        )

    def test_case2(self):
        value = testUtil.file_test(
            """8
6 2 8 -3 1 1 6 10
100""",
            task_2.main,
        )
        self.assertEqual(
            set(value.strip().split()),
            {"None"},
        )


if __name__ == "__main__":
    unittest.main()
