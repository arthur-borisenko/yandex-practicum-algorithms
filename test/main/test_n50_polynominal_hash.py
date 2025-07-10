import unittest

import main.main.solution_n50_polynominal_hash as solution
from test.utils import testUtil


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
