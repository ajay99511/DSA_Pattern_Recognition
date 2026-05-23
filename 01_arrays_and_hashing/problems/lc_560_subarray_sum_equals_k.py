"""
## Problem: Subarray Sum Equals K (LC #560)
- **Pattern**: Arrays & Hashing - Prefix Sum + Hash Map
- **Difficulty**: Medium
- **Key Insight**: A subarray nums[j+1..i] sums to k iff prefix[i] - prefix[j] == k, i.e., prefix[j] == prefix[i] - k; tracking how many times each prefix sum has appeared lets us count valid subarrays in O(1) per element.
- **Recognition Signal**: "count subarrays with sum equal to k" / "number of subarrays summing to target" → prefix sum + hash map
- **Complexity**: Time O(N), Space O(N)
- **My Confidence**: 🟡
- **Review Dates**: [date1] → [date2] → [date3]
"""

# STEP-BY-STEP APPROACH:
# 1. Initialize prefix_count = {0: 1}.
#    WHY {0: 1}: a prefix sum of 0 "appeared once" before index 0,
#    which handles subarrays that start at index 0.
# 2. Maintain curr_sum (running prefix sum) and result counter.
# 3. For each num:
#    a. curr_sum += num
#    b. needed = curr_sum - k
#       If needed is in prefix_count, those are valid starting points → add count.
#    c. Increment prefix_count[curr_sum].
# 4. Return result.

# COMMON MISTAKE: Updating prefix_count BEFORE querying would count the current
# index as a valid starting point, leading to off-by-one errors.

# SOLUTION:
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_count = {0: 1}           # prefix_sum → number of times it has appeared
                                        # Seed with {0:1} to handle subarrays starting at index 0

        curr_sum = 0                    # Running prefix sum
        result = 0                      # Count of valid subarrays

        for num in nums:
            curr_sum += num             # Extend prefix sum to include current element

            needed = curr_sum - k       # If this prefix sum appeared before at index j,
                                        # then nums[j+1..current] sums to k

            result += prefix_count.get(needed, 0)   # Add count of valid starting points

            # Update AFTER querying to avoid counting current index as its own start
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

        return result


# TEST CASES:
if __name__ == "__main__":
    s = Solution()

    # Classic: [1,1] and [1,1] (indices 0-1 and 1-2) both sum to 2
    assert s.subarraySum([1, 1, 1], 2) == 2,        "three ones, k=2"

    # Two subarrays: [3] and [1,2]
    assert s.subarraySum([1, 2, 3], 3) == 2,        "k=3, two subarrays"

    # No match
    assert s.subarraySum([1], 0) == 0,              "no match"

    # Negative numbers
    assert s.subarraySum([-1, -1, 1], 0) == 1,      "negatives, k=0"

    # k=0 with zeros in array
    assert s.subarraySum([0, 0, 0], 0) == 6,        "all zeros, k=0: 6 subarrays"

    # Single element equals k
    assert s.subarraySum([5], 5) == 1,              "single element equals k"

    # Entire array sums to k
    assert s.subarraySum([1, 2, 3], 6) == 1,        "entire array"

    # Large k — no match
    assert s.subarraySum([1, 2, 3], 100) == 0,      "k too large"

    print("✅ All tests passed!")
