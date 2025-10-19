from utils import testUtil
import unittest



import main.sprint_4.n50_D_polynominal_hash.solution as solution
from utils import testUtil




class TestCase(unittest.TestCase):

    def test_case1(self):
        value = testUtil.file_test(
            """123
100003
a
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """97
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """123
100003
HaSH
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """56156
""".rstrip(),
        )
