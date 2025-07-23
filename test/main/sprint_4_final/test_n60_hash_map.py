import unittest

import main.main.sprint_4_final.solution_n60_hash_map as solution
from test.utils import testUtil


class TestCase(unittest.TestCase):

    def test_case1(self):
        value = testUtil.file_test(
            """10
get 1
put 1 10
put 2 4
get 1
get 2
delete 2
get 2
put 1 5
get 1
delete 2
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """None
10
4
4
None
5
None
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """8
get 9
delete 9
put 9 1
get 9
put 9 2
get 9
put 9 3
get 9
""",
            solution.main,
        )
        self.assertEqual(
            value.rstrip(),
            """None
None
1
2
3""".rstrip(),
        )
