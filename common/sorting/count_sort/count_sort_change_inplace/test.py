from common.util import tester
from . import implementation


class TestCountSort(tester.SortTester):
    def test_already_sorted(self):
        inp_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        test_arr = inp_arr.copy()
        self._patch_sorted(implementation.count_sort, test_arr)
        self._checker(inp_arr, test_arr)

    def test_reversed_input(self):
        inp_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        test_arr = inp_arr.copy()
        self._patch_sorted(implementation.count_sort, test_arr)
        self._checker(inp_arr, test_arr)

    def test_empty(self):
        inp_arr = []
        test_arr = inp_arr.copy()
        self._patch_sorted(implementation.count_sort, test_arr)
        self._checker(inp_arr, test_arr)

    def test_random_order(self):
        inp_arr = [7, 3, 9, 5, 1, 5, 2, 6, 4, 8, 8]
        test_arr = inp_arr.copy()
        self._patch_sorted(implementation.count_sort, test_arr)
        self._checker(inp_arr, test_arr)

    def test_nulls(self):
        inp_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        test_arr = inp_arr.copy()
        self._patch_sorted(implementation.count_sort, test_arr)
        self._checker(inp_arr, test_arr)


class TestCountSortReversed(tester.SortTester):
    def test_already_sorted(self):
        inp_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        test_arr = inp_arr.copy()
        self._patch_sorted(implementation.count_sort, test_arr, reverse=True)
        self._checker(inp_arr, test_arr, reverse=True)

    def test_reversed_input(self):
        inp_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        test_arr = inp_arr.copy()
        self._patch_sorted(implementation.count_sort, test_arr, reverse=True)
        self._checker(inp_arr, test_arr, reverse=True)

    def test_empty(self):
        inp_arr = []
        test_arr = inp_arr.copy()
        self._patch_sorted(implementation.count_sort, test_arr, reverse=True)
        self._checker(inp_arr, test_arr, reverse=True)

    def test_random_order(self):
        inp_arr = [7, 3, 9, 5, 1, 5, 2, 6, 4, 8, 8]
        test_arr = inp_arr.copy()
        self._patch_sorted(implementation.count_sort, test_arr, reverse=True)
        self._checker(inp_arr, test_arr, reverse=True)

    def test_nulls(self):
        inp_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        test_arr = inp_arr.copy()
        self._patch_sorted(implementation.count_sort, test_arr, reverse=True)
        self._checker(inp_arr, test_arr, reverse=True)
