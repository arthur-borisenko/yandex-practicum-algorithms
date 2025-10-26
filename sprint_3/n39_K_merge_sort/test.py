import unittest


import unittest.mock as mock
import sprint_3.n39_K_merge_sort.solution as task


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


class TestFromContest(unittest.TestCase):
    def test(self):
        a = [1, 4, 9, 2, 10, 11]
        b = task.merge(a, 0, 3, 6)
        expected = [1, 2, 4, 9, 10, 11]
        self.assertEqual(b, expected)
        c = [1, 4, 2, 10, 1, 2]
        task.merge_sort(c, 0, 6)
        expected = [1, 1, 2, 2, 4, 10]
        self.assertEqual(c, expected)
