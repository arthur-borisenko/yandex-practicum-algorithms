import unittest


import sprint_4.n56_K_nearest_station.solution as task
from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """3
-1 0
1 0
2 5
3
10 0
20 0
22 5

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
            """3
-1 0
1 0
0 5
3
10 0
20 0
20 5

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
