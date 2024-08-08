import task
import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """1010
1011
""",
            task.main,
        )
        self.assertEqual(
            value,
            """10101
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """1
1
            """,
            task.main,
        )
        self.assertEqual(
            value,
            """10
""",
        )


if __name__ == "__main__":
    unittest.main()
