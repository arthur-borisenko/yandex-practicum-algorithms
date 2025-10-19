from utils import testUtil
import main.sprint_6.n77_A_build_adjacency_list.solution as task


import unittest

from utils import testUtil


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
            """1 3
1 3
0
0
1 2
""".rstrip(),
        )


if __name__ == "__main__":
    unittest.main()
