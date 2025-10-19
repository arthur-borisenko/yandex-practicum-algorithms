from utils import testUtil
import main.sprint_3.n38_J_bubble.solution as task


import unittest

from utils import testUtil




class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5
4 3 9 2 1
""",
            task.main,
        )
        self.assertEqual(
            value,
            """3 4 2 1 9
3 2 1 4 9
2 1 3 4 9
1 2 3 4 9
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """5
12 8 9 10 11
""",
            task.main,
        )
        self.assertEqual(
            value,
            """8 9 10 11 12
""",
        )


if __name__ == "__main__":
    unittest.main()
