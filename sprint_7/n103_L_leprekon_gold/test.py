import unittest


import sprint_7.n103_L_leprekon_gold.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5 15
3 8 1 2 5

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """15

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """5 19
10 10 7 7 4

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """18

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
