import task
import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3 1
""",
            task.main,
        )
        self.assertEqual(
            value,
            """3
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """0 100
""",
            task.main,
        )
        self.assertEqual(
            value,
            """1
""",
        )

    def test_case3(self):
        value = testUtil.file_test(
            """11 2
""",
            task.main,
        )
        self.assertEqual(
            value,
            """44
""",
        )


if __name__ == "__main__":
    unittest.main()
