from utils import testUtil
import unittest


import main.sprint_8.n117_I_repeat.solution as task
from utils import testUtil




class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """zzzzzz

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """6

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """abacaba

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
            """abababab

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """4

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
