from utils import testUtil
import unittest


import main.sprint_7.n101_K_goroskopy.solution as task
from utils import testUtil




class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5
4 9 2 4 6
7
9 4 0 0 2 8 4

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3
2 3 4
1 5 7

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """4
1 1 1 1
2
2 2

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """0

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """8
1 2 1 9 1 2 1 9
5
9 9 1 9 9

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3
4 7 8
1 3 5

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
