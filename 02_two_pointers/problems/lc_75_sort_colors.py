"""
## Problem: Sort Colors (LC #75)
- **Pattern**: Two Pointers - Partition (Dutch National Flag)
- **Difficulty**: Medium
- **Key Insight**: Three pointers divide the array into four regions (0s, 1s, unknown, 2s); the mid cursor processes each element exactly once, making it a single-pass O(N) sort.
- **Recognition Signal**: "sort array of 0s, 1s, 2s" / "in-place" / "one pass" → Dutch National Flag 3-pointer partition
- **Complexity**: Time O(N), Space O(1)
- **My Confidence**: 🟡
- **Review Dates**: [date1] → [date2] → [date3]
"""

# Problem: Given an array nums with values 0, 1, or 2, sort it in-place so that
# all 0s come first, then 1s, then 2s. Must be done in a single pass without
# using the built-in sort function.

# STEP-BY-STEP APPROACH:
# 1. low = 0 (right boundary of the 0-region, exclusive).
#    mid = 0 (current element under examination).
#    high = n-1 (left boundary of the 2-region, exclusive).
# 2. While mid <= high (unknown region is non-empty):
#    a. nums[mid] == 0 → swap(low, mid), low++, mid++ (swapped-in element is known to be 1).
#    b. nums[mid] == 1 → mid++ (already in correct middle region).
#    c. nums[mid] == 2 → swap(mid, high), high-- (do NOT advance mid; swapped-in element is unknown).
# 3. Loop ends when mid > high → all elements are classified.

# NOTE: The critical subtlety — after swapping with high, mid does NOT advance
# because the element that came from nums[high] has not been examined yet.
# After swapping with low, mid DOES advance because nums[low] was in the
# [low..mid-1] region (all 1s), so the swapped-in element is known to be 1.

from typing import List


def sort_colors(nums: List[int]) -> None:
    """Modifies nums in-place; returns None."""
    low  = 0                              # WHY: exclusive right boundary of the 0-region
    mid  = 0                              # WHY: current element under examination (scan cursor)
    high = len(nums) - 1                  # WHY: exclusive left boundary of the 2-region

    while mid <= high:                    # WHY <=: stop when the unknown region [mid..high] is empty
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]   # WHY: move 0 to the left region
            low  += 1                     # WHY: expand 0-region rightward
            mid  += 1                     # WHY: element now at mid came from [low..mid-1] → it's a 1; safe to advance
        elif nums[mid] == 1:
            mid  += 1                     # WHY: 1 is already in the correct middle region
        else:                             # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid] # WHY: move 2 to the right region
            high -= 1                     # WHY: expand 2-region leftward
                                          # WHY NOT mid++: element swapped in from high is unexamined


# TEST CASES:
if __name__ == "__main__":
    # Standard LC example
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2], "standard case"

    # Minimal 3-element case
    nums = [2, 0, 1]
    sort_colors(nums)
    assert nums == [0, 1, 2],          "three elements"

    # Single element
    nums = [0]
    sort_colors(nums)
    assert nums == [0],                "single 0"

    # All same value
    nums = [1, 1, 1]
    sort_colors(nums)
    assert nums == [1, 1, 1],          "all 1s"

    # Already sorted
    nums = [0, 0, 1, 1, 2, 2]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2], "already sorted"

    # Reverse sorted
    nums = [2, 2, 1, 1, 0, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2], "reverse sorted"

    print("✅ All tests passed!")
