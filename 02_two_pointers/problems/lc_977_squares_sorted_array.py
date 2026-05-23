"""
## Problem: Squares of a Sorted Array (LC #977)
- **Pattern**: Two Pointers - Opposite Direction
- **Difficulty**: Medium
- **Key Insight**: The largest squares come from the ends of the sorted array (most negative or most positive); fill the result array from the back using two pointers converging inward.
- **Recognition Signal**: "sorted array with negatives" + "return sorted squares" → opposite-direction pointers filling result from the back
- **Complexity**: Time O(N), Space O(N) for the output array
- **My Confidence**: 🟢
- **Review Dates**: [date1] → [date2] → [date3]
"""

# Problem: Given an integer array nums sorted in non-decreasing order, return an
# array of the squares of each number, also sorted in non-decreasing order.

# STEP-BY-STEP APPROACH:
# 1. left = 0, right = n-1, pos = n-1 (fill result from the back).
# 2. While left <= right:
#    a. Compare abs(nums[left]) with abs(nums[right]).
#    b. Place the larger square at result[pos], decrement pos.
#    c. Advance the pointer whose absolute value was larger.
# 3. Return result.

# NOTE: Filling from the back avoids the need to reverse the array at the end.
# The largest square always comes from one of the two ends because the array
# is sorted — negatives are on the left, positives on the right.

from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n                          # WHY pre-allocate: fill from back in O(1) per step
    left, right = 0, n - 1
    pos = n - 1                               # WHY start at n-1: largest square goes to the last slot

    while left <= right:                      # WHY <=: process all elements including when pointers meet
        left_sq  = nums[left]  ** 2
        right_sq = nums[right] ** 2

        if left_sq > right_sq:
            result[pos] = left_sq             # WHY: left end has the larger square
            left += 1                         # WHY: consume the left element
        else:
            result[pos] = right_sq            # WHY: right end has the larger (or equal) square
            right -= 1                        # WHY: consume the right element

        pos -= 1                              # WHY: move to the next slot from the back

    return result


# TEST CASES:
if __name__ == "__main__":
    # Mix of negatives and positives
    assert sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100], "mixed"

    # All negatives
    assert sorted_squares([-7, -3, -1])        == [1, 9, 49],         "all negatives"

    # All positives
    assert sorted_squares([1, 2, 3, 4])        == [1, 4, 9, 16],      "all positives"

    # Single element
    assert sorted_squares([5])                 == [25],                "single element"

    # Contains zero
    assert sorted_squares([-3, -2, 0, 2, 3])  == [0, 4, 4, 9, 9],    "symmetric with zero"

    print("✅ All tests passed!")
