"""Binary Search — Reusable Templates"""
from typing import List
from bisect import bisect_left, bisect_right


def binary_search(nums: List[int], target: int) -> int:
    """Classic: find exact target. O(log N)."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target: return mid
        elif nums[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1


def lower_bound(nums: List[int], target: int) -> int:
    """First index where nums[i] >= target."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target: lo = mid + 1
        else: hi = mid
    return lo


def upper_bound(nums: List[int], target: int) -> int:
    """First index where nums[i] > target."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] <= target: lo = mid + 1
        else: hi = mid
    return lo


def search_rotated(nums: List[int], target: int) -> int:
    """LC #33 — Search in rotated sorted array."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target: return mid
        if nums[lo] <= nums[mid]:  # Left half is sorted
            if nums[lo] <= target < nums[mid]: hi = mid - 1
            else: lo = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[hi]: lo = mid + 1
            else: hi = mid - 1
    return -1


def find_min_rotated(nums: List[int]) -> int:
    """LC #153 — Find minimum in rotated sorted array."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]: lo = mid + 1
        else: hi = mid
    return nums[lo]


def koko_eating_bananas(piles: List[int], h: int) -> int:
    """LC #875 — Binary search on answer (eating speed)."""
    def can_finish(speed):
        return sum((p + speed - 1) // speed for p in piles) <= h
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_finish(mid): hi = mid
        else: lo = mid + 1
    return lo


if __name__ == "__main__":
    assert binary_search([1,3,5,7,9], 5) == 2
    assert binary_search([1,3,5,7,9], 4) == -1
    assert lower_bound([1,3,5,5,5,7], 5) == 2
    assert upper_bound([1,3,5,5,5,7], 5) == 5
    assert search_rotated([4,5,6,7,0,1,2], 0) == 4
    assert find_min_rotated([3,4,5,1,2]) == 1
    assert koko_eating_bananas([3,6,7,11], 8) == 4
    print("✅ All binary search templates passed!")
