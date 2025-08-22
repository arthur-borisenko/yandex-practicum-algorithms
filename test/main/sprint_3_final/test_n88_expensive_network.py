import unittest
import main.main.sprint_6_final.solution_n88_expensive_network as task
from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """4 4
1 2 5
1 3 6
2 4 8
3 4 3
""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """19

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3 3
1 2 1
1 2 2
2 3 1
""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """2 0

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """Oops! I did it again

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
