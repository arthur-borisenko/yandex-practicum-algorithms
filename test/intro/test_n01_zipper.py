import unittest
from main.intro.n01_zipper import task
from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.mockAndRun(
            """3
1 2 3
4 5 6""".splitlines(),
            task.main,
        )
        self.assertEqual(
            value.strip(),
            """1 4 2 5 3 6""",
        )


if __name__ == "__main__":
    unittest.main()
