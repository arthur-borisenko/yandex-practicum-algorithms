import unittest
import main.main.solution_n56_nearest_station as task
from test.utils import testUtil


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
