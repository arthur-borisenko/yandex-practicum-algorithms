import sprint_2.n15_A_management.solution as task


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
""",
            task.main,
        )
        self.assertEqual(
            value,
            """1 0 7 2
2 2 4 7
3 6 1 0
""",
        )

    def test_case2(self):
        value = testUtil.file_test(
            """9
5
-7 -1 0 -4 -9
5 -1 2 2 9
3 1 -8 -1 -7
9 0 8 -8 -1
2 4 5 2 8
-7 10 0 -4 -8
-3 10 -7 10 3
1 6 -7 -5 9
-1 9 9 1 9
""",
            task.main,
        )
        self.assertEqual(
            value,
            """-7 5 3 9 2 -7 -3 1 -1
-1 -1 1 0 4 10 10 6 9
0 2 -8 8 5 0 -7 -7 9
-4 2 -1 -8 2 -4 10 -5 1
-9 9 -7 -1 8 -8 3 9 9
""",
        )

    def test_time_and_big_values(self):
        time_limit = float("inf")
        inp_matrix = []
        exc_matrix = []
        for i in range(1000):
            inp_matrix.append([998] * 1000)
            exc_matrix.append([998] * 1000)
        inp_matrix[0][1] = 1000
        exc_matrix[1][0] = 1000
        inp_matrix_str = "\n".join(map(lambda x: " ".join(map(str, x)), inp_matrix))
        exc_matrix_str = "\n".join(map(lambda x: " ".join(map(str, x)), exc_matrix))
        input_data = f"""{10**3}
{10**3}
{inp_matrix_str}"""
        output = exc_matrix_str

        value, sol_time = testUtil.time_file_test(
            input_data,
            task.main,
        )
        print(
            f"solution time is {round(sol_time, 2)} seconds, limit is {time_limit} seconds"
        )
        self.assertLess(sol_time, time_limit)
        self.assertEqual(
            value,
            output + "\n",
        )


if __name__ == "__main__":
    unittest.main()
