import task
import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """1 2 -3
""",
            task.main,
        )
        self.assertEqual(
            value.strip(),
            """FAIL""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            f"""{10**9} {-10**9} 2""",
            task.main,
        )
        self.assertEqual(value.strip(), """WIN""")


if __name__ == "__main__":
    unittest.main()
