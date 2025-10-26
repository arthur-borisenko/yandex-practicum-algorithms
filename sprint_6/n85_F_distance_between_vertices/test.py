import unittest
import sprint_6.n85_F_distance_between_vertices.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5 5
2 4
3 5
2 1
2 3
4 5
1 5

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """3

""".rstrip(),
        )

    def test_case2(self):
        value = testUtil.file_test(
            """4 3
2 3
4 3
2 4
1 3

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """-1

""".rstrip(),
        )

    def test_case3(self):
        value = testUtil.file_test(
            """2 1
2 1
1 1

""".rstrip(),
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """0

""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
