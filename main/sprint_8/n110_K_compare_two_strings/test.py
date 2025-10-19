from utils import testUtil
import unittest


import main.sprint_8.n110_K_compare_two_strings.solution as task
from utils import testUtil




class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """gggggbbb
bbef

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """-1

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """z
aaaaaaa

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """1

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """ccccz
aaaaaz

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
