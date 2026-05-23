"""
## Problem: 4Sum (LC #18)
- **Pattern**: Two Pointers - Opposite Direction
- **Difficulty**: Medium
- **Key Insight**: Extend 3Sum by adding one more fixed outer loop; sort first, fix two elements with nested loops, then run two-pointer on the remaining subarray — skip duplicates at every level.
- **Recognition Signal**: "find all unique quadruplets that sum to target" → sort + two fixed loops + two-pointer; generalization of 3Sum
- **Complexity**: Time O(N³), Space O(1) excluding output
- **My Confidence**: 🟡
- **Review Dates**: [date1] → [date2] → [date3]
"""

# Problem: Given an integer array nums and an integer target, return all unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that a, b, c, d are
# distinct indices and nums[a] + nums[b] + nums[c] + nums[d] == target.

# STEP-BY-STEP APPROACH:
# 1. Sort nums.
# 2. Outer loop: fix i from 0 to n-4; skip duplicate nums[i].
# 3. Inner loop: fix j from i+1 to n-3; skip duplicate nums[j].
# 4. Two-pointer: left = j+1, right = n-1.
#    a. Compute total = nums[i] + nums[j] + nums[left] + nums[right].
#    b. If total == target → record quadruplet, skip duplicates, advance both pointers.
#    c. If total < target → left++.
#    d. If total > target → right--.
# 5. Return all quadruplets.

# NOTE: Duplicate skipping must happen at all three levels (i, j, and the
# inner two-pointer) to guarantee unique quadruplets without a set.

from typing import List


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()                                         # WHY sort: enables two-pointer + duplicate skipping
    result = []
    n = len(nums)

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:            # WHY: skip duplicate first elements
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:   # WHY: skip duplicate second elements
                continue

            left, right = j + 1, n - 1                 # WHY: two-pointer on the remaining subarray

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:   # WHY: skip dup left
                        left += 1
                    while left < right and nums[right] == nums[right - 1]: # WHY: skip dup right
                        right -= 1
                    left  += 1                          # WHY: advance past the matched pair
                    right -= 1

                elif total < target:
                    left  += 1                          # WHY: sum too small; need larger left
                else:
                    right -= 1                          # WHY: sum too large; need smaller right

    return result


# TEST CASES:
if __name__ == "__main__":
    # Standard case
    result = four_sum([1, 0, -1, 0, -2, 2], 0)
    assert sorted(result) == sorted([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]), "standard"

    # All zeros
    assert four_sum([0, 0, 0, 0], 0) == [[0, 0, 0, 0]],  "all zeros"

    # No valid quadruplets
    assert four_sum([1, 2, 3, 4], 100) == [],             "no solution"

    # Negative target
    result = four_sum([-3, -2, -1, 0, 0, 1, 2, 3], 0)
    assert [-3, -2, 2, 3] in result,                      "negative target, check one quadruplet"

    # Minimum size input (exactly 4 elements)
    assert four_sum([2, 2, 2, 2], 8) == [[2, 2, 2, 2]],  "four equal elements"

    print("✅ All tests passed!")
