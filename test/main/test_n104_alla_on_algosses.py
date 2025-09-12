import unittest
import main.main.solution_n104_alla_on_algosses as task
from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """130
4
10 3 40 1

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """4

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """100
2
7 5

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """16

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """1
1
1

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
