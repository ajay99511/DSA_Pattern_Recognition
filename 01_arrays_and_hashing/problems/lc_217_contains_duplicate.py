"""
## Problem: Contains Duplicate (LC #217)
- **Pattern**: Arrays & Hashing - Set for Existence
- **Difficulty**: Easy
- **Key Insight**: A set gives O(1) membership checks; if we ever try to add a number that's already in the set, we found a duplicate.
- **Recognition Signal**: "contains duplicate" / "any value appears more than once" → set for existence
- **Complexity**: Time O(N), Space O(N)
- **My Confidence**: 🟢
- **Review Dates**: [date1] → [date2] → [date3]
"""

# STEP-BY-STEP APPROACH:
# 1. Create an empty set to track numbers we've seen.
# 2. Iterate through each number in the array.
# 3. If the number is already in the set → return True (duplicate found).
# 4. Otherwise, add the number to the set and continue.
# 5. If we finish the loop without finding a duplicate → return False.

# SOLUTION:
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()                    # O(1) average-case add and membership check

        for num in nums:
            if num in seen:             # Already encountered this number → duplicate
                return True
            seen.add(num)               # Record for future checks

        return False                    # No duplicate found


# TEST CASES:
if __name__ == "__main__":
    s = Solution()

    # Basic duplicate
    assert s.containsDuplicate([1, 2, 3, 1]) == True,  "duplicate at end"

    # All unique
    assert s.containsDuplicate([1, 2, 3, 4]) == False, "all unique"

    # Single element — can't be a duplicate
    assert s.containsDuplicate([1]) == False,           "single element"

    # Empty array
    assert s.containsDuplicate([]) == False,            "empty array"

    # All same
    assert s.containsDuplicate([5, 5, 5, 5]) == True,  "all same"

    # Duplicate at the very start
    assert s.containsDuplicate([2, 2, 1, 3]) == True,  "duplicate at start"

    print("✅ All tests passed!")
