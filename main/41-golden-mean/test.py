import task
import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """2
1
1 3
2
""",
            task.main,
        )
        self.assertEqual(
            value.strip(),
            """2
""".strip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """2
2
1 2
3 4
""",
            task.main,
        )
        self.assertEqual(
            value.strip(),
            """2.5
""".strip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """8
10
0 0 0 1 3 3 5 10
4 4 5 7 7 7 8 9 9 10
""",
            task.main,
        )
        self.assertEqual(
            value.strip(),
            """5
""".strip(),
        )

    def test_case4(self):
        value = testUtil.file_test(
            f"""10000
10000
{("10000 "*4).strip()}
{("9999 "*4).strip()}
""",
            task.main,
        )
        self.assertEqual(
            value.strip(),
            """9999.5
""".strip(),
        )


if __name__ == "__main__":
    unittest.main()
