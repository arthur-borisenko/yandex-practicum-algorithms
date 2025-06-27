def _search_bad(l, left, right):
    if left > right:
        raise Exception
    mid=left+(right-left)//2
    if mid+1<len(l) and l[mid] > l[mid+1]:
        return mid
    elif left==right:
        raise Exception
    if l[mid] > l[right]:
        return search_bad(l, mid + 1, right)
    else:
        return search_bad(l, left, mid)
def search_bad(l, left, right):
    if l[left]<=l[right]:
        return -1 # Already sorted
    return _search_bad(l, left, right)
class RingArrayShiftWrapper:
    def __init__(self, arr, shift):
        self.arr = arr
        self.shift = shift
    def calc_index(self, i):
        return (i+self.shift)%len(self.arr)
    def __len__(self):
        return len(self.arr)
    def __getitem__(self, i):
        return self.arr[self.calc_index(i)]
    def __setitem__(self, i, val):
        self.arr[self.calc_index(i)] = val
    def __iter__(self):
        class _Iterator:
            def __init__(self, seq):
                self.i=-1
                self.arr = seq
            def __iter__(self):
                return self
            def __next__(self):
                self.i+=1
                if self.i<len(self.arr):
                    return self.arr[self.i]
                raise StopIteration
        return _Iterator(self)
def search(arr, target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
def broken_search(nums, target) -> int:
    broken_index=search_bad(nums, 0, len(nums) - 1)
    if broken_index!=-1:
        seq=RingArrayShiftWrapper(nums, -(len(nums)-broken_index-1))
        i = search(seq, target)
        if i==-1:
            return -1
        index = seq.calc_index(i)
        return index
    else:
        i=search(nums, target)
        if i==-1:
            return -1
        return i



def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
