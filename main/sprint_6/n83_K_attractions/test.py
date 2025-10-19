from utils import testUtil
import main.sprint_6.n83_K_attractions.solution as task


import unittest

from utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """4 4
1 2 1
2 3 3
3 4 5
1 4 2
""",
            task.main,
        )
        self.assertEqual(
            value,
            """0 1 4 2 
1 0 3 3 
4 3 0 5 
2 3 5 0 
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """3 2
1 2 1
1 2 2
""",
            task.main,
        )
        self.assertEqual(
            value,
            """0 1 -1 
1 0 -1 
-1 -1 0 
""",
        )

    def test_case3(self):
        value = testUtil.file_test(
            f"""2 0
""",
            task.main,
        )
        self.assertEqual(
            value,
            """0 -1 
-1 0 
""",
        )


if __name__ == "__main__":
    unittest.main()
