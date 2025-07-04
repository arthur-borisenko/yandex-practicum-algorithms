def broken_search(nums, target) -> int:
    """CPU - O(log n)(but with a little better constant)
    RAM - O(1)"""
    left, right = 0, len(nums) - 1  # initialization.
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:  # Base case.
            return mid
        if nums[left] <= nums[mid]:  # Checks if the left-mid segment is sorted.
            if (
                nums[left] <= target < nums[mid]
            ):  # check if the target is in the left-mid segment.
                right = mid - 1  # move referrers to left-mid
            else:
                left = mid + 1  # otherwise target may be only in mid-right segment
        else:
            if (
                nums[mid] < target <= nums[right]
            ):  # check if the target may be in the mid-right segment.
                left = mid + 1  # move referrers to mid-right
            else:
                right = mid - 1  # otherwise target may be only in left-mid segment
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


test()
