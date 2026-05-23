"""
## Problem: Top K Frequent Elements (LC #347)
- **Pattern**: Arrays & Hashing - Frequency Map + Bucket Sort
- **Difficulty**: Medium
- **Key Insight**: Bucket sort by frequency (buckets indexed 1..N) lets us collect the top-K elements in O(N) by scanning buckets from highest to lowest — no heap needed.
- **Recognition Signal**: "top K frequent" / "most common K elements" → Counter + bucket sort for O(N), or Counter + heap for O(N log K)
- **Complexity**: Time O(N), Space O(N)
- **My Confidence**: 🟢
- **Review Dates**: [date1] → [date2] → [date3]
"""

# STEP-BY-STEP APPROACH (Bucket Sort — O(N)):
# 1. Build a frequency map: Counter(nums) → {value: count}.
# 2. Create N+1 buckets (index = frequency). Max frequency is N (all elements identical).
# 3. For each (value, count) in the frequency map, append value to buckets[count].
# 4. Scan buckets from index N down to 1, collecting values until we have K elements.
# 5. Return the collected K elements.

# ALTERNATIVE (Heap — O(N log K)):
# heapq.nlargest(k, freq.keys(), key=freq.get)
# Faster when k << N, but not strictly O(N).

# SOLUTION:
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)                    # {value: count} — O(N)

        # Bucket sort: buckets[i] holds all values that appear exactly i times
        # Max frequency is len(nums), so we need len(nums)+1 buckets (0-indexed)
        buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]

        for value, count in freq.items():
            buckets[count].append(value)        # Place value in its frequency bucket

        result = []
        # Scan from highest frequency bucket down to 1
        for i in range(len(buckets) - 1, 0, -1):
            for value in buckets[i]:
                result.append(value)
                if len(result) == k:            # Early exit once we have k elements
                    return result

        return result                           # Fallback (k <= len(nums) guaranteed)

    # --- Alternative: Heap approach O(N log K) ---
    def topKFrequent_heap(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        # heapq.nlargest maintains a min-heap of size k → O(N log k)
        return heapq.nlargest(k, freq.keys(), key=freq.get)


# TEST CASES:
if __name__ == "__main__":
    s = Solution()

    # Classic: 1 appears 3x, 2 appears 2x, 3 appears 1x → top 2 = [1, 2]
    assert set(s.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}, "classic top-2"

    # Single element
    assert s.topKFrequent([1], 1) == [1], "single element"

    # k equals total unique elements
    assert set(s.topKFrequent([1, 2], 2)) == {1, 2}, "k = all unique"

    # All same element
    assert s.topKFrequent([5, 5, 5, 5], 1) == [5], "all same"

    # Top 1 from varied frequencies
    assert s.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2) == s.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)

    # Heap alternative
    assert set(s.topKFrequent_heap([1, 1, 1, 2, 2, 3], 2)) == {1, 2}, "heap top-2"
    assert s.topKFrequent_heap([1], 1) == [1], "heap single"

    print("✅ All tests passed!")
