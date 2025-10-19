from utils import testUtil
import unittest


import main.sprint_7.n105_G_bankomat.solution as task
from utils import testUtil




class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5
3
3 2 1
""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """5

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3
2
2 1
""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """8
1
5
""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """0

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
