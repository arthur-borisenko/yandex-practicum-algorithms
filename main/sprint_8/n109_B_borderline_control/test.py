from utils import testUtil
import unittest


import main.sprint_8.n109_B_borderline_control.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """abcdefg
abdefg

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """OK

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """helo
hello

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """OK

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """dog
fog

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """OK

""".rstrip(),
        )

    def test_case4(self):
        value = testUtil.file_test(
            """mama
papa

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """FAIL

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
