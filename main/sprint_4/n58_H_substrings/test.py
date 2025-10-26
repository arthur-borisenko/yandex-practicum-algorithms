from utils import testUtil
import unittest


import main.sprint_4.n58_H_substrings.solution as solution
from utils import testUtil


class TestCase(unittest.TestCase):

    def test_case1(self):
        value = testUtil.file_test(
            """ojodx
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """4
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """abbabcabcbb
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3
""".rstrip(),
        )
