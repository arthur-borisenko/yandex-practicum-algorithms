from utils import testUtil
import unittest


import main.sprint_7.n97_M_backpack.solution as task
from utils import testUtil




class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """4 6
2 7
4 2
1 5
2 1

""".rstrip(),
            task.main,
        )
        lines = value.splitlines()
        assert len(lines) >= 2
        self.assertEqual(3, int(lines[0]))
        self.assertListEqual(
            sorted(list(map(int, lines[1].split())), reverse=True), [4, 3, 1]
        )


if __name__ == "__main__":
    unittest.main()
