from utils import testUtil
import unittest


import main.sprint_5.n63_I_different_search_trees.solution as solution
from utils import testUtil


class TestCase(unittest.TestCase):

    def test_case1(self):
        value = testUtil.file_test(
            """4
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """14
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """5
""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """2""",
            solution.main,
        )
        self.assertEqual(value.rstrip(), """2""".rstrip())
