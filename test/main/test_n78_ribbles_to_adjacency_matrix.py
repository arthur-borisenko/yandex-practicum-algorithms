from main.main import solution_n78_ribbles_to_adjacency_matrix as task
import unittest

from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """5 3
1 3
2 3
5 2
""",
            task.main,
        )
        self.assertEqual(
            value.rstrip(),
            """0 0 1 0 0
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
