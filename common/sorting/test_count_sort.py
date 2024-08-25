import unittest
from . import tester, count_sort


class TestCountSorted(tester.SortTester):
    def test_case1(self):
        inp_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = self._patch_sorted(count_sort.count_sorted, inp_arr)
        self._checker(inp_arr, res)

    def test_case2(self):
        inp_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        res = self._patch_sorted(count_sort.count_sorted, inp_arr)
        self._checker(inp_arr, res)

    def test_case3(self):
        inp_arr = []
        res = self._patch_sorted(count_sort.count_sorted, inp_arr)
        self._checker(inp_arr, res)

    def test_case4(self):
        inp_arr = [7, 3, 9, 5, 1, 5, 2, 6, 4, 8, 8]
        res = self._patch_sorted(count_sort.count_sorted, inp_arr)
        self._checker(inp_arr, res)

    def test_case5(self):
        inp_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        res = self._patch_sorted(count_sort.count_sorted, inp_arr)
        self._checker(inp_arr, res)

    def test_case1rev(self):
        inp_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = self._patch_sorted(count_sort.count_sorted, inp_arr, reverse=True)
        self._checker(inp_arr, res, reverse=True)

    def test_case2rev(self):
        inp_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        res = self._patch_sorted(count_sort.count_sorted, inp_arr, reverse=True)
        self._checker(inp_arr, res, reverse=True)

    def test_case3rev(self):
        inp_arr = []
        res = self._patch_sorted(count_sort.count_sorted, inp_arr, reverse=True)
        self._checker(inp_arr, res, reverse=True)

    def test_case4rev(self):
        inp_arr = [7, 3, 9, 5, 1, 5, 2, 6, 4, 8, 8]
        res = self._patch_sorted(count_sort.count_sorted, inp_arr, reverse=True)
        self._checker(inp_arr, res, reverse=True)

    def test_case5rev(self):
        inp_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        res = self._patch_sorted(count_sort.count_sorted, inp_arr, reverse=True)
        self._checker(inp_arr, res, reverse=True)


class TestCountSort(tester.SortTester):
    def test_case1(self):
        inp_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        test_arr = inp_arr.copy()
        self._patch_sorted(count_sort.count_sort, test_arr)
        self._checker(inp_arr, test_arr)

    def test_case2(self):
        inp_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        test_arr = inp_arr.copy()
        self._patch_sorted(count_sort.count_sort, test_arr)
        self._checker(inp_arr, test_arr)

    def test_case3(self):
        inp_arr = []
        test_arr = inp_arr.copy()
        self._patch_sorted(count_sort.count_sort, test_arr)
        self._checker(inp_arr, test_arr)

    def test_case4(self):
        inp_arr = [7, 3, 9, 5, 1, 5, 2, 6, 4, 8, 8]
        test_arr = inp_arr.copy()
        self._patch_sorted(count_sort.count_sort, test_arr)
        self._checker(inp_arr, test_arr)

    def test_case5(self):
        inp_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        test_arr = inp_arr.copy()
        self._patch_sorted(count_sort.count_sort, test_arr)
        self._checker(inp_arr, test_arr)

    def test_case1rev(self):
        inp_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        test_arr = inp_arr.copy()
        self._patch_sorted(count_sort.count_sort, test_arr, reverse=True)
        self._checker(inp_arr, test_arr, reverse=True)

    def test_case2rev(self):
        inp_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        test_arr = inp_arr.copy()
        self._patch_sorted(count_sort.count_sort, test_arr, reverse=True)
        self._checker(inp_arr, test_arr, reverse=True)

    def test_case3rev(self):
        inp_arr = []
        test_arr = inp_arr.copy()
        self._patch_sorted(count_sort.count_sort, test_arr, reverse=True)
        self._checker(inp_arr, test_arr, reverse=True)

    def test_case4rev(self):
        inp_arr = [7, 3, 9, 5, 1, 5, 2, 6, 4, 8, 8]
        test_arr = inp_arr.copy()
        self._patch_sorted(count_sort.count_sort, test_arr, reverse=True)
        self._checker(inp_arr, test_arr, reverse=True)

    def test_case5rev(self):
        inp_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        test_arr = inp_arr.copy()
        self._patch_sorted(count_sort.count_sort, test_arr, reverse=True)
        self._checker(inp_arr, test_arr, reverse=True)
