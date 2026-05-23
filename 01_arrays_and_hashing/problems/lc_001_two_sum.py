"""
## Problem: Two Sum (LC #1)
- **Pattern**: Arrays & Hashing - Complement Lookup
- **Difficulty**: Easy
- **Key Insight**: For each number, the complement (target - num) is what we need; storing seen values in a hash map lets us check for the complement in O(1) instead of scanning the rest of the array.
- **Recognition Signal**: "find two numbers that add to target" / "return indices of pair" → complement lookup with hash map
- **Complexity**: Time O(N), Space O(N)
- **My Confidence**: 🟢
- **Review Dates**: [date1] → [date2] → [date3]
"""

# STEP-BY-STEP APPROACH:
# 1. Create a hash map: value → index (to retrieve the index of the complement).
# 2. For each element nums[i]:
#    a. Compute complement = target - nums[i].
#    b. If complement is already in the map → return [map[complement], i].
#    c. Otherwise, store nums[i] → i in the map.
# 3. Problem guarantees exactly one solution, so we always return inside the loop.

# NOTE: Store AFTER checking to avoid pairing an element with itself
# (e.g., target=6, nums=[3,3] — we need two different indices).

# SOLUTION:
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}                           # Maps value → index for O(1) complement lookup

        for i, num in enumerate(nums):
            complement = target - num       # What value do we need to complete the pair?

            if complement in seen:          # O(1) check — did we see the complement earlier?
                return [seen[complement], i]  # Return both indices; seen[complement] is the earlier one

            seen[num] = i                   # Store AFTER checking to avoid self-pairing

        return []                           # Unreachable: problem guarantees exactly one solution


# TEST CASES:
if __name__ == "__main__":
    s = Solution()

    # Basic case
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1],  "basic: 2+7=9"

    # Complement appears later
    assert s.twoSum([3, 2, 4], 6) == [1, 2],       "complement later: 2+4=6"

    # Same value at two different indices
    assert s.twoSum([3, 3], 6) == [0, 1],           "duplicate values: 3+3=6"

    # Negative numbers
    assert s.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4],  "negatives: -3+-5=-8"

    # Zero involved
    assert s.twoSum([0, 4, 3, 0], 0) == [0, 3],    "zeros: 0+0=0"

    # Multiple valid pairs — algorithm returns the first one found (1+7=8 at indices [0,3])
    # The complement lookup finds 7 when processing index 3 (seen={1:0,5:1,3:2})
    result = s.twoSum([1, 5, 3, 7], 8)
    assert result in [[0, 3], [1, 2]], "multiple valid pairs — first found"

    print("✅ All tests passed!")
