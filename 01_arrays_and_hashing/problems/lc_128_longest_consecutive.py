"""
## Problem: Longest Consecutive Sequence (LC #128)
- **Pattern**: Arrays & Hashing - Set + Sequence Start Trick
- **Difficulty**: Medium
- **Key Insight**: Convert to a set for O(1) lookups, then only start counting from the beginning of each sequence (where num-1 is NOT in the set); this ensures each element is visited at most twice, giving O(N) total.
- **Recognition Signal**: "longest consecutive sequence" / "O(N) time required" → set + start-of-sequence trick
- **Complexity**: Time O(N), Space O(N)
- **My Confidence**: 🟢
- **Review Dates**: [date1] → [date2] → [date3]
"""

# STEP-BY-STEP APPROACH:
# 1. Convert nums to a set (deduplicates and gives O(1) lookups).
# 2. For each num in the set:
#    a. Skip if num-1 is in the set (num is not the start of a sequence).
#    b. If num IS the start, count how far the sequence extends:
#       while num+length in set: length += 1
#    c. Update longest = max(longest, length).
# 3. Return longest.

# WHY "start of sequence" trick: without it, we'd recount every sequence
# from every element → O(N²). By only starting from sequence beginnings,
# each element is touched at most twice (once as a start check, once during extension).

# SOLUTION:
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)             # O(N) build; O(1) membership checks; deduplicates

        longest = 0

        for num in num_set:             # Iterate over set to avoid processing duplicates
            # Only start counting from the beginning of a sequence
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:  # Extend sequence as far as it goes
                    length += 1
                longest = max(longest, length)

        return longest


# TEST CASES:
if __name__ == "__main__":
    s = Solution()

    # Classic: 1,2,3,4 is the longest sequence (length 4)
    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4,          "classic"

    # Long sequence: 0-8 (length 9)
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9, "long sequence"

    # Empty array
    assert s.longestConsecutive([]) == 0,                               "empty"

    # Single element
    assert s.longestConsecutive([5]) == 1,                              "single element"

    # All same element (duplicates)
    assert s.longestConsecutive([1, 1, 1, 1]) == 1,                    "all duplicates"

    # Already consecutive
    assert s.longestConsecutive([1, 2, 3, 4, 5]) == 5,                 "already sorted consecutive"

    # Negative numbers
    assert s.longestConsecutive([-3, -2, -1, 0, 1]) == 5,              "negatives"

    # Two separate sequences of equal length
    assert s.longestConsecutive([1, 2, 3, 10, 11, 12]) == 3,           "two equal sequences"

    print("✅ All tests passed!")
