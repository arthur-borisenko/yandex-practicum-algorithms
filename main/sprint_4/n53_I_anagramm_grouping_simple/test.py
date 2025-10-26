from utils import testUtil
import unittest


import main.sprint_4.n53_I_anagramm_grouping_simple.solution as solution
from utils import testUtil


class TestCase(unittest.TestCase):

    def test_case1(self):
        value = testUtil.file_test(
            """6
tan eat tea ate nat bat
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """0 4
1 2 3
5
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """11
5228 8225 @#$% #%$@ 8252 5282 $@#% %$@# agaf faga aafg
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """0 1 4 5
2 3 6 7
8 9 10
""".rstrip(),
        )
