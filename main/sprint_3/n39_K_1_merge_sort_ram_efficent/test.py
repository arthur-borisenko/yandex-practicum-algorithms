from utils import testUtil
import unittest


import unittest.mock as mock
import main.sprint_3.n39_K_1_merge_sort_ram_efficent.solution as task

class TestMergeSort(unittest.TestCase):
    def _checker(self, i, o):
        exp = sorted(i)
        self.assertEqual(o, exp)

    def _runner(self, i, m):
        test_arr = i.copy()
        with mock.patch(
            "builtins.sorted",
            mock.Mock(
                side_effect=AssertionError(
                    "Built-in sorting methods may not be used in solution"
                )
            ),
        ):
            m(test_arr, 0, len(test_arr))
        self._checker(i, test_arr)

    def test_case1(self):
        input = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self._runner(input, task.merge_sort)

    def test_case2(self):
        input = []
        self._runner(input, task.merge_sort)

    def test_case3(self):
        input = [1, 1, 1, 1, 1]
        self._runner(input, task.merge_sort)
