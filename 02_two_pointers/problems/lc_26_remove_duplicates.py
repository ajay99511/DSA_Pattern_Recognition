"""
## Problem: Remove Duplicates from Sorted Array (LC #26)
- **Pattern**: Two Pointers - Same Direction
- **Difficulty**: Medium
- **Key Insight**: A slow write pointer maintains the "clean" unique prefix; the fast read pointer only writes to slow when it finds a value different from the current unique tail.
- **Recognition Signal**: "remove duplicates in-place" / "sorted array" / "return new length" → fast/slow write pointer; sorted order guarantees duplicates are adjacent
- **Complexity**: Time O(N), Space O(1)
- **My Confidence**: 🟢
- **Review Dates**: [date1] → [date2] → [date3]
"""

# Problem: Given a sorted integer array nums, remove duplicates in-place so that
# each unique element appears only once. Return the number of unique elements k.
# The first k elements of nums must hold the result; the rest don't matter.

# STEP-BY-STEP APPROACH:
# 1. Handle empty array edge case → return 0.
# 2. slow = 0 (last written unique element index).
# 3. fast scans from index 1 to n-1.
# 4. When nums[fast] != nums[slow]:
#    a. slow += 1 (advance write pointer to next slot).
#    b. nums[slow] = nums[fast] (write the new unique element).
# 5. Return slow + 1 (length = last valid index + 1).

# NOTE: We compare nums[fast] against nums[slow] (not nums[fast-1]) because
# slow is the tail of the clean prefix, which may lag far behind fast.

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    slow = 0                              # WHY slow=0: first element is always unique and kept

    for fast in range(1, len(nums)):      # WHY start at 1: compare each element against the clean tail
        if nums[fast] != nums[slow]:      # WHY !=: found a new unique element not yet in the prefix
            slow += 1                     # WHY slow++: advance write pointer to the next open slot
            nums[slow] = nums[fast]       # WHY write: place the new unique element in the clean prefix

    return slow + 1                       # WHY +1: slow is the last valid index; length = index + 1


# TEST CASES:
if __name__ == "__main__":
    # Two duplicates at the start
    nums = [1, 1, 2]
    k = remove_duplicates(nums)
    assert k == 2 and nums[:k] == [1, 2],                    "[1,1,2] → [1,2]"

    # Multiple duplicates
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    assert k == 5 and nums[:k] == [0, 1, 2, 3, 4],          "multiple duplicates"

    # Single element — already unique
    nums = [1]
    k = remove_duplicates(nums)
    assert k == 1 and nums[:k] == [1],                       "single element"

    # All unique — no changes needed
    nums = [1, 2, 3, 4, 5]
    k = remove_duplicates(nums)
    assert k == 5 and nums[:k] == [1, 2, 3, 4, 5],          "all unique"

    # All same value
    nums = [7, 7, 7, 7]
    k = remove_duplicates(nums)
    assert k == 1 and nums[:k] == [7],                       "all same"

    print("✅ All tests passed!")
