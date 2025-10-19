from utils import testUtil
import unittest


import main.sprint_8.n115_G_search_with_shift.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """9
3 9 1 2 5 10 9 1 7
2
4 10

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """1 8

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """5
1 2 3 4 5
3
10 11 12

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """1 2 3

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
