import task
import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3
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
            """0
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
