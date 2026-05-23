"""
## Problem: Move Zeroes (LC #283)
- **Pattern**: Two Pointers - Same Direction
- **Difficulty**: Easy
- **Key Insight**: Use a slow write pointer that only advances when a non-zero is found; swapping (not overwriting) automatically pushes zeros to the back without a second pass.
- **Recognition Signal**: "move all 0s to end" / "preserve relative order" / "in-place" → fast/slow write pointer with swap
- **Complexity**: Time O(N), Space O(1)
- **My Confidence**: 🟢
- **Review Dates**: [date1] → [date2] → [date3]
"""

# Problem: Given an integer array nums, move all 0s to the end while maintaining
# the relative order of the non-zero elements. Must be done in-place.

# STEP-BY-STEP APPROACH:
# 1. slow = 0 (next write position for a non-zero element).
# 2. fast scans every index from 0 to n-1.
# 3. When nums[fast] != 0:
#    a. Swap nums[slow] with nums[fast].
#    b. Increment slow.
# 4. After the loop, nums[0..slow-1] holds all non-zeros in original order,
#    and nums[slow..n-1] holds all zeros.

# NOTE: Swapping instead of assigning means we never need a second pass to
# fill zeros — the zero that was at nums[slow] gets pushed to nums[fast].


def move_zeroes(nums: list) -> None:
    """Modifies nums in-place; returns None."""
    slow = 0                              # WHY: next slot for a non-zero element

    for fast in range(len(nums)):
        if nums[fast] != 0:               # WHY: only act on non-zero elements
            nums[slow], nums[fast] = nums[fast], nums[slow]  # WHY swap: zero drifts right automatically
            slow += 1                     # WHY: advance write pointer past the placed non-zero


# TEST CASES:
if __name__ == "__main__":
    # Standard case
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    assert nums == [1, 3, 12, 0, 0],  "standard case"

    # Single zero
    nums = [0]
    move_zeroes(nums)
    assert nums == [0],               "single zero"

    # No zeros — array unchanged
    nums = [1, 2, 3]
    move_zeroes(nums)
    assert nums == [1, 2, 3],         "no zeros"

    # All zeros
    nums = [0, 0, 0]
    move_zeroes(nums)
    assert nums == [0, 0, 0],         "all zeros"

    # Leading zeros
    nums = [0, 0, 0, 1]
    move_zeroes(nums)
    assert nums == [1, 0, 0, 0],      "leading zeros"

    print("✅ All tests passed!")
