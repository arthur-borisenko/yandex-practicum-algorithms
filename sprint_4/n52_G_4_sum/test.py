from utils import testUtil
import unittest


import sprint_4.n52_G_4_sum.solution as task


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """6
0
1 0 -1 0 2 -2
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3
-2 -1 1 2
-2 0 0 2
-1 0 0 1
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """8
10
2 3 2 4 1 10 3 0
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3
0 3 3 4
1 2 3 4
2 2 3 3
""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """5
4
1 1 1 1 1
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """1
1 1 1 1
""".rstrip(),
        )

    def test_case4(self):
        value = testUtil.file_test(
            """9
10
1 2 3 4 100 4 3 2 1
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            # """0 27
            """3
1 1 4 4
1 2 3 4
2 2 3 3""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
