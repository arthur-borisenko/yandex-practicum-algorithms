import task
import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """7
1 2 3 1 2 3 4
3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """1 2 3
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """6
1 1 1 2 2 3
1
""",
            task.main,
        )
        self.assertEqual(
            value,
            """1
""",
        )


if __name__ == "__main__":
    unittest.main()
