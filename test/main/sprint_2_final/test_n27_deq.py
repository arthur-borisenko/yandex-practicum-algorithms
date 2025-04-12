import unittest
from main.main.sprint_2_final import solution_n27_deq as task
from test.utils import testUtil


class TestCase(unittest.TestCase):
    def test_case1(self):
        value = testUtil.file_test(
            """7
10
push_front -855
push_front 0
pop_back
pop_back
push_back 844
pop_back
push_back 823
""",
            task.main,
        )
        self.assertEqual(
            value,
            """-855
0
844
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """7
3
push_back 7
push_back 65
push_back 87
pop_back
push_back 83
pop_back
pop_front
""",
            task.main,
        )
        self.assertEqual(
            value,
            """87
83
7
""",
        )


if __name__ == "__main__":
    unittest.main()
