import unittest


import sprint_7.n96_I_hard_flower_field.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """2 3
101
110

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3
RRU

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3 3
100
110
001

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2
URRU
""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
