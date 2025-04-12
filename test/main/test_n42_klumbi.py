import unittest
from main.main import solution_n42_klumbi as task
from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """4
7 8
7 8
2 3
6 10
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2 3
6 10
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """4
2 3
5 6
3 4
3 4
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2 4
5 6
""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """6
1 3
3 5
4 6
5 6
2 4
7 10
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """1 6
7 10
""".rstrip(),
        )

    def test_case4(self):
        value = testUtil.file_test(
            #             """14
            # 16 24
            # 19 23
            # 13 18
            # 15 23
            # 8 10
            # 0 14
            # 20 27
            # 4 26
            # 2 13
            # 5 21
            # 3 6
            # 7 17
            # 1 9
            # 11 26
            # """,
            """14
68 87
81 85
62 76
66 85
47 53
4 65
82 96
23 92
10 62
33 84
21 42
43 70
9 50
58 92
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            # """0 27
            """4 96""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
