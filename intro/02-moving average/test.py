import unittest, task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.mockAndRun(
            """7
1 2 3 4 5 6 7
4""".splitlines(),
            task.main,
        )
        self.assertEqual(
            value.strip(),
            """2.5 3.5 4.5 5.5""",
        )


if __name__ == "__main__":
    unittest.main()
