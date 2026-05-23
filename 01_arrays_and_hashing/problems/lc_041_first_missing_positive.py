"""
## Problem: First Missing Positive (LC #41)
- **Pattern**: Arrays & Hashing - Array as Hash Map (Index Encoding)
- **Difficulty**: Hard
- **Key Insight**: The answer must be in [1, N+1]; use the array itself as a hash map by negating nums[v-1] to mark that value v is present — this achieves O(N) time with O(1) extra space.
- **Recognition Signal**: "first missing positive" / "O(N) time O(1) space" → use the array as its own hash map
- **Complexity**: Time O(N), Space O(1) extra
- **My Confidence**: 🔴
- **Review Dates**: [date1] → [date2] → [date3]
"""

# STEP-BY-STEP APPROACH:
#
# KEY OBSERVATION: The answer is always in [1, N+1].
#   - If all of 1..N are present → answer is N+1.
#   - Otherwise → answer is the first missing value in 1..N.
#
# STEP 1 — Sanitize: Replace all values ≤ 0 or > N with N+1 (out-of-range sentinel).
#   WHY: These values can't be the answer and would corrupt our index encoding.
#
# STEP 2 — Mark: For each value v = abs(nums[i]) in [1, N]:
#   Negate nums[v-1] to encode "value v has been seen".
#   WHY abs(): the value may already be negative from a previous mark.
#   WHY check > 0 before negating: avoid double-negating (which would undo the mark).
#
# STEP 3 — Find: Scan for the first index i where nums[i] > 0.
#   That index+1 is the first missing positive.
#   If all are negative → return N+1.

# SOLUTION:
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        # Step 1: Replace out-of-range values with n+1 (safe sentinel)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1         # n+1 is out of [1,N] range; won't interfere with marking

        # Step 2: Mark presence of values in [1, N] by negating at the target index
        for i in range(n):
            val = abs(nums[i])          # Use abs() — value may already be negative from prior mark
            if 1 <= val <= n:
                idx = val - 1           # Value v maps to index v-1 (0-indexed)
                if nums[idx] > 0:       # Only negate if positive (avoid double-negation)
                    nums[idx] = -nums[idx]

        # Step 3: First index with a positive value → that index+1 is missing
        for i in range(n):
            if nums[i] > 0:
                return i + 1            # i+1 was never marked → it's the first missing positive

        return n + 1                    # All values 1..N are present → answer is N+1


# TEST CASES:
if __name__ == "__main__":
    s = Solution()

    # LeetCode examples
    assert s.firstMissingPositive([1, 2, 0])         == 3, "[1,2,0] → 3"
    assert s.firstMissingPositive([3, 4, -1, 1])     == 2, "[3,4,-1,1] → 2"
    assert s.firstMissingPositive([7, 8, 9, 11, 12]) == 1, "[7,8,9,11,12] → 1"

    # Single element
    assert s.firstMissingPositive([1])               == 2, "[1] → 2"
    assert s.firstMissingPositive([2])               == 1, "[2] → 1"

    # All negatives
    assert s.firstMissingPositive([-1, -2, -3])      == 1, "all negatives → 1"

    # Consecutive from 1
    assert s.firstMissingPositive([1, 2, 3, 4, 5])  == 6, "1..5 → 6"

    # Duplicates
    assert s.firstMissingPositive([1, 1, 2, 2])      == 3, "duplicates → 3"

    # Large gap
    assert s.firstMissingPositive([1000])            == 1, "large value → 1"

    # Mixed
    assert s.firstMissingPositive([0, 2, 2, 1, 1])  == 3, "mixed with zeros → 3"

    print("✅ All tests passed!")
