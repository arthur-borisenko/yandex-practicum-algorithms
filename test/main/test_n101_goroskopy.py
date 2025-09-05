import unittest
import main.main.solution_n101_goroskopy as task
from test.utils import testUtil


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
1 3 4
2 5 7

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
3 4 8
3 4 5

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
