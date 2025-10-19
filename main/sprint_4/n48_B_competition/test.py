import unittest
import main.sprint_4.n48_B_competition.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """2
0 1

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3
0 1 0

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
