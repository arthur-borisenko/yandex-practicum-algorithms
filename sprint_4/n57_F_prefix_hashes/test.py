import unittest


import sprint_4.n57_F_prefix_hashes.solution as solution
from utils import testUtil


class TestCase(unittest.TestCase):

    def test_case1(self):
        value = testUtil.file_test(
            """1000
1000009
abcdefgh
7
1 1
1 5
2 3
3 4
4 4
1 8
5 8
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """97
225076
98099
99100
100
436420
193195
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """100
10
a
1
1 1
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """7
""".rstrip(),
        )
