from utils import testUtil
import unittest



import main.sprint_4.n55_L_mnogogosha.solution as solution
from utils import testUtil




class TestCase(unittest.TestCase):

    def test_case1(self):
        value = testUtil.file_test(
            """10 2
gggggooooogggggoooooogggggssshaa
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """0 5
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3 4
allallallallalla
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """0 1 2
""".rstrip(),
        )
