import task
import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """2
1 2
3
2 1 3
""",
            task.main,
        )
        self.assertEqual(
            value,
            """2
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3
2 1 3
2
1 1
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
            f"""10000
{" ".join(map(str,range(10000)))}
10000
{" ".join(map(str,range(10000)))}
""",
            task.main,
        )
        self.assertEqual(
            value,
            """10000
""",
        )


if __name__ == "__main__":
    unittest.main()
