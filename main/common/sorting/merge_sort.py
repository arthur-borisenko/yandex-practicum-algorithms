class MergeSort(list):
    def __init__(self, _iterable, reverse=False):
        super().__init__(_iterable)
        self._merge_sort(self, 0, len(self))
        if reverse:
            self[:] = reversed(self)

    def _merge_sort(self, arr, lf, rg):
        """CPU - O(n log(n))
        RAM - O(log(n))
        n - interval length"""
        if rg - lf > 1:
            mid = (rg + lf) // 2
            self._merge_sort(arr, lf, mid)
            self._merge_sort(arr, mid, rg)
            arr[lf:rg] = self._merge(arr, lf, mid, rg)

    @staticmethod
    def _merge(arr, lf, mid, rg):
        def select_array(_arr, _lf, _mid, _left_i, _right_i, _left_len, _right_len):
            return (
                1
                if _left_i < mid and (_right_i >= rg or _arr[left_i] <= _arr[right_i])
                else 2
            )

        left_len = mid - lf
        right_len = rg - mid
        append_i = 0
        res = [0] * (rg - lf)
        left_i, right_i = lf, mid
        for i in range(left_len + right_len):
            if select_array(arr, lf, mid, left_i, right_i, left_len, right_len) == 1:
                res[append_i] = arr[left_i]
                append_i += 1
                left_i += 1
            else:
                res[append_i] = arr[right_i]
                append_i += 1
                right_i += 1
        return res
