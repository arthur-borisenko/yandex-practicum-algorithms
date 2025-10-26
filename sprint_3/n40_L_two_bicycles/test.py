import unittest
import sprint_3.n40_L_two_bicycles.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """6
1 2 4 4 6 8
3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """3 5
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """6
1 2 4 4 4 4
3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """3 -1
""",
        )

    def test_case3(self):
        value = testUtil.file_test(
            """10
2 2 2 2 2 2 2 2 2 2
1
""",
            task.main,
        )
        self.assertEqual(
            value,
            """1 1
""",
        )


if __name__ == "__main__":
    unittest.main()
