import unittest


import sprint_7.n104_E_alla_on_algosses.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """130
4
10 3 40 1

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """4

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """100
2
7 5

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """16

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """1
1
1

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """1

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
