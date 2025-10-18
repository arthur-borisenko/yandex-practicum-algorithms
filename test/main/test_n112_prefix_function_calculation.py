import unittest
import main.main.solution_n112_prefix_function_calculation as task
from test.utils import testUtil


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
