"""
## Problem: 3Sum Closest (LC #16)
- **Pattern**: Two Pointers - Opposite Direction
- **Difficulty**: Medium
- **Key Insight**: Sort first, then for each fixed element run a two-pointer sweep tracking the closest sum seen so far; the sorted order lets us move pointers intelligently toward the target.
- **Recognition Signal**: "find triplet with sum closest to target" → sort + fix + two-pointer; same structure as 3Sum but track minimum absolute difference instead of exact match
- **Complexity**: Time O(N²), Space O(1)
- **My Confidence**: 🟡
- **Review Dates**: [date1] → [date2] → [date3]
"""

# Problem: Given an integer array nums and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three integers.
# Assume exactly one solution exists.

# STEP-BY-STEP APPROACH:
# 1. Sort nums.
# 2. Initialize closest = nums[0] + nums[1] + nums[2] (first valid triplet).
# 3. For each index i from 0 to n-3:
#    a. left = i+1, right = n-1.
#    b. While left < right:
#       - Compute curr = nums[i] + nums[left] + nums[right].
#       - If |curr - target| < |closest - target| → update closest.
#       - If curr == target → return target immediately (can't get closer).
#       - If curr < target → left++ (need a larger sum).
#       - If curr > target → right-- (need a smaller sum).
# 4. Return closest.

# NOTE: Unlike 3Sum, we don't need to skip duplicates here because we're
# tracking the closest value, not collecting unique triplets.

from typing import List


def three_sum_closest(nums: List[int], target: int) -> int:
    nums.sort()                                         # WHY sort: enables two-pointer direction logic
    closest = nums[0] + nums[1] + nums[2]               # WHY: initialize with a valid triplet sum

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1             # WHY: two-pointer on the subarray after i

        while left < right:
            curr = nums[i] + nums[left] + nums[right]

            if abs(curr - target) < abs(closest - target):  # WHY: found a closer sum
                closest = curr

            if curr == target:
                return target                           # WHY: exact match → can't get any closer

            elif curr < target:
                left  += 1                              # WHY: sum too small; move left to increase it
            else:
                right -= 1                              # WHY: sum too large; move right to decrease it

    return closest


# TEST CASES:
if __name__ == "__main__":
    # Standard case
    assert three_sum_closest([-1, 2, 1, -4], 1) == 2,   "standard: -1+2+1=2, closest to 1"

    # Exact match exists
    assert three_sum_closest([0, 0, 0], 1)       == 0,   "all zeros, target=1"

    # Negative target
    assert three_sum_closest([1, 1, 1, 0], -100) == 2,   "negative target: 0+1+1=2"

    # Large positive target
    assert three_sum_closest([1, 2, 3, 4], 100)  == 9,   "large target: 2+3+4=9"

    # Three elements only
    assert three_sum_closest([1, 2, 4], 4)        == 7,   "three elements: 1+2+4=7"

    print("✅ All tests passed!")
