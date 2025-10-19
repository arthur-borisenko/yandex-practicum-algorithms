import unittest
import main.sprint_7_final.solution_n107_levenstain_distance as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """abacaba
abaabc

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """innokentiy
innnokkentia

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """r
x

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
