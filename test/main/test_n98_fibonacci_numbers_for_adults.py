import unittest
import main.main.solution_n98_fibonacci_numbers_for_adults as task
from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """8

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """2

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
            """10

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """89

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
