import unittest
import main.sprint_6_final.solution_n89_water_world as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3 3
#.#
.#.
#.#
""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """5 1

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """4 5
#####
.#...
..#..
#####
""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """2 6
""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
