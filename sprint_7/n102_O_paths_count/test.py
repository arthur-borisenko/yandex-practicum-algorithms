import unittest


import sprint_7.n102_O_paths_count.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3 3
1 2
1 2
2 3
1 3

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """5 3
1 2
3 4
4 5
1 5

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
            """3 3
1 2
2 3
1 3
1 1

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """1

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
