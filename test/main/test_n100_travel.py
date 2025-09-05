import unittest
import main.main.solution_n100_travel as task
from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5
4 2 9 1 13

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3
1 3 5

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """6
1 2 4 8 16 32

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """6
1 2 3 4 5 6

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
