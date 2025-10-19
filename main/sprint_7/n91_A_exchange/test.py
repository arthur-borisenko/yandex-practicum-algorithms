from utils import testUtil
import unittest


import main.sprint_7.n91_A_exchange.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """6
7 1 5 3 6 4
""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """7

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """5
1 2 3 4 5
""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """4

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """6
1 12 12 16 1 8
""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """22

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
