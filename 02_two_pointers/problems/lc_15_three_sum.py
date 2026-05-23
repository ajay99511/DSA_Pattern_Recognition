"""
## Problem: 3Sum (LC #15)
- **Pattern**: Two Pointers - Opposite Direction
- **Difficulty**: Medium
- **Key Insight**: Sort first, then fix one element and reduce to a Two Sum II problem on the remaining subarray; skip duplicates at both the outer and inner levels to avoid duplicate triplets.
- **Recognition Signal**: "find all unique triplets that sum to zero" / "no duplicate triplets" → sort + fix + two-pointer sweep
- **Complexity**: Time O(N²), Space O(1) excluding output
- **My Confidence**: 🟡
- **Review Dates**: [date1] → [date2] → [date3]
"""

# Problem: Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
# such that i != j != k and nums[i] + nums[j] + nums[k] == 0.
# The solution set must not contain duplicate triplets.

# STEP-BY-STEP APPROACH:
# 1. Sort nums — enables two-pointer and easy duplicate skipping.
# 2. For each index i from 0 to n-3:
#    a. Skip if nums[i] == nums[i-1] (duplicate outer element).
#    b. Early exit if nums[i] > 0 (sorted → remaining elements are all positive → no zero sum possible).
#    c. Run Two Sum II on nums[i+1 .. n-1] with target = -nums[i].
#    d. When a triplet is found, skip duplicate left and right values before continuing.
# 3. Collect all valid triplets.

# NOTE: Sorting is the key enabler — it makes duplicate skipping trivial
# and allows the two-pointer technique on the inner subarray.

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()                                     # WHY sort: enables two-pointer + duplicate skipping
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:        # WHY: skip duplicate outer elements
            continue
        if nums[i] > 0:                             # WHY: sorted → all remaining are positive → no zero sum
            break

        left, right = i + 1, len(nums) - 1         # WHY: two-pointer on the subarray after i

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates on both sides before continuing
                while left < right and nums[left] == nums[left + 1]:   # WHY: avoid duplicate triplets
                    left += 1
                while left < right and nums[right] == nums[right - 1]: # WHY: same reason from right
                    right -= 1
                left  += 1                          # WHY: move past the matched pair
                right -= 1

            elif total < 0:
                left  += 1                          # WHY: sum too small; need a larger left value
            else:
                right -= 1                          # WHY: sum too large; need a smaller right value

    return result


# TEST CASES:
if __name__ == "__main__":
    # Standard case with multiple triplets
    result = three_sum([-1, 0, 1, 2, -1, -4])
    assert sorted(result) == sorted([[-1, -1, 2], [-1, 0, 1]]), "standard case"

    # No valid triplets
    assert three_sum([0, 1, 1]) == [],                            "no triplets"

    # All zeros
    assert three_sum([0, 0, 0]) == [[0, 0, 0]],                  "all zeros"

    # All same non-zero value
    assert three_sum([1, 1, 1]) == [],                            "all same positive"

    # Negative and positive mix
    result = three_sum([-4, -1, -1, 0, 1, 2])
    assert sorted(result) == sorted([[-1, -1, 2], [-1, 0, 1]]),  "negative/positive mix"

    print("✅ All tests passed!")
