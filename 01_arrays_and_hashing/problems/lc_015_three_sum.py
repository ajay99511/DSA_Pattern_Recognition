"""
## Problem: 3Sum (LC #15)
- **Pattern**: Arrays & Hashing - Sort + Two Pointers (with hash map alternative)
- **Difficulty**: Medium
- **Key Insight**: Sort the array, then for each element nums[i], use two pointers on the remaining subarray to find pairs that sum to -nums[i]; skip duplicates at each level to avoid duplicate triplets.
- **Recognition Signal**: "find all unique triplets that sum to zero" / "three numbers summing to target" → sort + two pointers
- **Complexity**: Time O(N²), Space O(1) extra (excluding output)
- **My Confidence**: 🟡
- **Review Dates**: [date1] → [date2] → [date3]
"""

# STEP-BY-STEP APPROACH (Sort + Two Pointers):
# 1. Sort nums — enables two-pointer technique and easy duplicate skipping.
# 2. For each index i from 0 to N-3:
#    a. Skip if nums[i] == nums[i-1] (duplicate first element → same triplets).
#    b. Early exit if nums[i] > 0 (sorted array → no three positives sum to 0).
#    c. Set left = i+1, right = N-1.
#    d. While left < right:
#       - total = nums[i] + nums[left] + nums[right]
#       - If total == 0: record triplet, advance left/right, skip duplicates.
#       - If total < 0: left++ (need larger sum).
#       - If total > 0: right-- (need smaller sum).
# 3. Return all found triplets.

# HASH MAP ALTERNATIVE (O(N²) time, O(N) space):
# For each pair (i, j), check if -(nums[i]+nums[j]) exists in a set.
# Harder to deduplicate — two-pointer approach is cleaner for this problem.

# SOLUTION:
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()                         # Sort enables two pointers and duplicate skipping
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate first elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Early exit: smallest remaining element is positive → no valid triplet
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1               # Move both pointers inward
                    right -= 1

                elif total < 0:
                    left += 1               # Sum too small → increase left
                else:
                    right -= 1              # Sum too large → decrease right

        return result


# TEST CASES:
if __name__ == "__main__":
    s = Solution()

    def normalize(triplets):
        """Sort each triplet and the list for deterministic comparison."""
        return sorted([sorted(t) for t in triplets])

    # Classic: [-1,0,1] and [-1,-1,2]
    assert normalize(s.threeSum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]], "classic"

    # No valid triplet
    assert s.threeSum([0, 1, 1]) == [], "no valid triplet"

    # All zeros
    assert normalize(s.threeSum([0, 0, 0])) == [[0, 0, 0]], "all zeros"

    # All same non-zero
    assert s.threeSum([1, 1, 1]) == [], "all same positive"

    # Two elements — can't form triplet
    assert s.threeSum([1, -1]) == [], "too few elements"

    # Multiple duplicates
    result = s.threeSum([-2, 0, 0, 2, 2])
    assert normalize(result) == [[-2, 0, 2]], "duplicates in input"

    # Negative heavy
    result = s.threeSum([-4, -1, -1, 0, 1, 2])
    assert normalize(result) == [[-1, -1, 2], [-1, 0, 1]], "negative heavy"

    print("✅ All tests passed!")
