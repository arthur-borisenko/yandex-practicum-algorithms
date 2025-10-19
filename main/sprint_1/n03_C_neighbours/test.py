from utils import testUtil
import main.sprint_1.n03_C_neighbours.solution as task


import unittest

from utils import testUtil




class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """4
3
1 2 3
0 2 6
7 4 1
2 7 0
3
0
""",
            task.main,
        )
        self.assertEqual(
            value.strip(),
            """7 7""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """4
3
1 2 3
0 2 6
7 4 1
2 7 0
0
0
""",
            task.main,
        )
        self.assertEqual(value.strip(), """0 2""")


if __name__ == "__main__":
    unittest.main()
