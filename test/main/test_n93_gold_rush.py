import unittest
import main.main.solution_n93_gold_rush as task
from test.utils import testUtil


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
