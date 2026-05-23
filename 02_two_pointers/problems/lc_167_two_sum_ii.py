"""
## Problem: Two Sum II - Input Array Is Sorted (LC #167)
- **Pattern**: Two Pointers - Opposite Direction
- **Difficulty**: Medium
- **Key Insight**: Sorted order gives a monotonic relationship — moving left right increases the sum, moving right left decreases it — so we can eliminate one candidate per step in O(N).
- **Recognition Signal**: "sorted array" + "find pair that sums to target" → opposite-direction pointers; O(N) beats the O(N²) brute force
- **Complexity**: Time O(N), Space O(1)
- **My Confidence**: 🟢
- **Review Dates**: [date1] → [date2] → [date3]
"""

# Problem: Given a 1-indexed sorted array of integers and a target, return the
# 1-indexed positions [index1, index2] of the two numbers that add up to target.
# Exactly one solution exists; you may not use the same element twice.

# STEP-BY-STEP APPROACH:
# 1. left = 0, right = len(numbers) - 1.
# 2. While left < right:
#    a. Compute curr_sum = numbers[left] + numbers[right].
#    b. If curr_sum == target → return [left+1, right+1] (1-indexed).
#    c. If curr_sum < target → left += 1 (need a larger value).
#    d. If curr_sum > target → right -= 1 (need a smaller value).
# 3. Problem guarantees a solution, so we always return inside the loop.

# NOTE: The sorted invariant is what makes this O(N). Without it, we'd need
# a hash map (O(N) space) or brute force (O(N²) time).

from typing import List


def two_sum_ii(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1          # WHY both ends: sorted array, converge inward

    while left < right:                         # WHY strict <: same element cannot be used twice
        curr_sum = numbers[left] + numbers[right]

        if curr_sum == target:
            return [left + 1, right + 1]        # WHY +1: problem uses 1-indexed output

        elif curr_sum < target:
            left += 1                           # WHY left++: sum too small; only a larger left helps
                                                # (right is already the largest available partner)
        else:
            right -= 1                          # WHY right--: sum too large; only a smaller right helps
                                                # (left is already the smallest available partner)

    return []                                   # Unreachable: problem guarantees exactly one solution


# TEST CASES:
if __name__ == "__main__":
    # Basic case
    assert two_sum_ii([2, 7, 11, 15], 9)  == [1, 2], "basic: 2+7=9"

    # Complement in the middle
    assert two_sum_ii([2, 3, 4], 6)        == [1, 3], "middle: 2+4=6"

    # Negative numbers
    assert two_sum_ii([-1, 0], -1)         == [1, 2], "negatives: -1+0=-1"

    # Duplicate values at different indices
    assert two_sum_ii([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5], "duplicates: 4+4=8"

    # Pair at the very ends (1-indexed: nums[0]=1 and nums[3]=20 → [1, 4])
    assert two_sum_ii([1, 5, 10, 20], 21) == [1, 4], "ends: 1+20=21 → [1,4]"

    print("✅ All tests passed!")
