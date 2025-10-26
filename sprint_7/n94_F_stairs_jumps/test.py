import unittest


import sprint_7.n94_F_stairs_jumps.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """6 3

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """13

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """7 7

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """32

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """2 2

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
