import unittest
import main.sprint_7_final.solution_n106_identical_sums as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """4
1 5 7 1

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """True
""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3
2 10 9

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """False
""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
