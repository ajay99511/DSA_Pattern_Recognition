"""
## Problem: 4Sum II (LC #454)
- **Pattern**: Arrays & Hashing - Hash Map of Pair Sums
- **Difficulty**: Hard
- **Key Insight**: Split the four arrays into two pairs; store all pairwise sums of (A, B) in a hash map with their counts, then for each pair sum from (C, D) check if its negation exists in the map — reduces O(N⁴) brute force to O(N²).
- **Recognition Signal**: "four arrays, count tuples summing to zero" / "4-array combination sum" → split into two pairs + hash map
- **Complexity**: Time O(N²), Space O(N²)
- **My Confidence**: 🟡
- **Review Dates**: [date1] → [date2] → [date3]
"""

# STEP-BY-STEP APPROACH:
# 1. Build a frequency map of all pairwise sums from arrays A and B:
#    ab_sums[a + b] += 1  for all a in A, b in B.
# 2. For each pair (c, d) from C × D:
#    needed = -(c + d)
#    If needed is in ab_sums, add ab_sums[needed] to the result count.
#    WHY: a + b + c + d == 0  ↔  a + b == -(c + d)
# 3. Return result.

# WHY split into two pairs: brute force is O(N⁴); splitting gives O(N²) for each half.
# This is the "meet in the middle" idea applied to hash maps.

# SOLUTION:
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int],
                     nums3: list[int], nums4: list[int]) -> int:
        ab_sums = defaultdict(int)          # Maps (a+b) → count of pairs producing that sum

        # Phase 1: Enumerate all pairs from nums1 × nums2
        for a in nums1:
            for b in nums2:
                ab_sums[a + b] += 1         # Record this pair sum

        result = 0

        # Phase 2: For each pair from nums3 × nums4, check if complement exists
        for c in nums3:
            for d in nums4:
                needed = -(c + d)           # We need a+b == -(c+d) for the total to be 0
                result += ab_sums[needed]   # Add count of (a,b) pairs that complete the tuple

        return result


# TEST CASES:
if __name__ == "__main__":
    s = Solution()

    # LeetCode example 1: answer = 2
    # Tuples: (0,0,0,0) and (1,-1,-1,1) → wait, let's verify
    # A=[1,2], B=[-2,-1], C=[-1,2], D=[0,2]
    # (1,-2,-1,2)=0 ✓, (2,-1,-1,0)=0 ✓ → 2
    assert s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2, "LC example 1"

    # LeetCode example 2: single zeros
    assert s.fourSumCount([0], [0], [0], [0]) == 1, "all zeros"

    # No valid tuples
    assert s.fourSumCount([1], [1], [1], [1]) == 0, "no valid tuples"

    # All elements the same non-zero value
    assert s.fourSumCount([1, 1], [-1, -1], [1, 1], [-1, -1]) == 16, "symmetric: 2*2*2*2=16"

    # Single elements summing to zero
    assert s.fourSumCount([1], [-1], [1], [-1]) == 1, "single elements"

    # Larger example
    result = s.fourSumCount([1, 2, -1], [-2, -1, 1], [1, -1, 2], [-1, 2, -2])
    assert isinstance(result, int) and result >= 0, "larger example returns non-negative int"

    print("✅ All tests passed!")
