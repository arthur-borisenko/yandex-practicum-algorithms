def search_bad(sequence, left=None, right=None):
    """Finds last element in left sorted part of the semi-sorted number array with unique with one or no disorder.
     If there is no disorder, returns -1.
     CPU - O(log n)
     RAM - O(log n)"""
    if left is None:
        left=0
    if right is None:
        right=len(sequence)-1
    if left > right:
        raise Exception
    if sequence[left] <= sequence[right]:
        return -1
    mid = left + (right - left) // 2
    if mid + 1 < len(sequence) and sequence[mid] > sequence[mid + 1]:
        return mid
    elif left == right:
        raise Exception
    if sequence[mid] > sequence[right]:
        return search_bad(sequence, mid + 1, right)
    else:
        return search_bad(sequence, left, mid)



class RingArrayShiftWrapper:
    def __init__(self, arr, shift):
        self.arr = arr
        self.shift = shift

    def calc_index(self, i):
        return (i + self.shift) % len(self.arr)

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, i):
        return self.arr[self.calc_index(i)]

    def __setitem__(self, i, val):
        self.arr[self.calc_index(i)] = val

    def __iter__(self):
        class _Iterator:
            def __init__(self, seq):
                self.i = -1
                self.arr = seq

            def __iter__(self):
                return self

            def __next__(self):
                self.i += 1
                if self.i < len(self.arr):
                    return self.arr[self.i]
                raise StopIteration

        return _Iterator(self)


def search(arr, target):
    """Classic binary search implementation.
    CPU - O(log n)
    RAM - O(log n)"""
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def broken_search(nums, target) -> int:
    """Finds element index in the semi-sorted number array with unique with one or no disorder.
         If there is no such element, returns -1.
         CPU - O(log n)
         RAM - O(log n)"""
    broken_index = search_bad(nums)
    if broken_index != -1:
        shift = -(len(nums) - broken_index - 1)
        wrapped_sequence = RingArrayShiftWrapper(nums, shift)
        broken_i = search(wrapped_sequence, target)
        if broken_i == -1:
            return -1
        index = wrapped_sequence.calc_index(broken_i)
        return index
    else:
        broken_i = search(nums, target)
        if broken_i == -1:
            return -1
        return broken_i


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
