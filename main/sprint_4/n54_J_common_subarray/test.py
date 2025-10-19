from utils import testUtil
import unittest



import main.sprint_4.n54_J_common_subarray.solution as solution
from utils import testUtil




class TestCase(unittest.TestCase):

    def test_case1(self):
        value = testUtil.file_test(
            """5
1 2 3 2 1
5
3 2 1 5 6
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """5
1 2 3 4 5
3
4 5 9
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2
""".rstrip(),
        )
