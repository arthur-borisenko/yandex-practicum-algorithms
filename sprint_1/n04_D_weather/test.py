import sprint_1.n04_D_weather.solution as task


import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """7
-1 -10 -8 0 2 0 5
""",
            task.main,
        )
        self.assertEqual(
            value.strip(),
            """3""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """5
1 2 5 4 8
""",
            task.main,
        )
        self.assertEqual(value.strip(), """2""")


if __name__ == "__main__":
    unittest.main()
