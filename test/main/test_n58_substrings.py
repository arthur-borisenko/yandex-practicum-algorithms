import unittest

import main.main.solution_n58_substrings as solution
from test.utils import testUtil


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
