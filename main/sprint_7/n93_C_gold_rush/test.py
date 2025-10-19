from utils import testUtil
import unittest


import main.sprint_7.n93_C_gold_rush.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """10
3
8 1
2 10
4 5

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """36

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """10000
1
4 20

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """80

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
