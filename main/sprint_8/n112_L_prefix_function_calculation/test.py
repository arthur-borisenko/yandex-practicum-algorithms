from utils import testUtil
import unittest


import main.sprint_8.n112_L_prefix_function_calculation.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """abracadabra

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """0 0 0 1 0 1 0 1 2 3 4 

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """xxzzxxz

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """0 1 0 0 1 2 3

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """aaaaa

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """0 1 2 3 4 

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
