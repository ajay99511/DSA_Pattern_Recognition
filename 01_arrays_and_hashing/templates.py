"""Arrays & Hashing — Reusable Templates"""
from collections import defaultdict, Counter
from typing import List
from itertools import accumulate


# ============================================================
# TEMPLATE 1: Hash Map Complement Lookup
# ============================================================
# USE WHEN: "Find pair/group that satisfies condition"
# TIME: O(N)  SPACE: O(N)

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}  # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# ============================================================
# TEMPLATE 2: Frequency Counting
# ============================================================
# USE WHEN: "Count occurrences", "most/least frequent", "anagram"
# TIME: O(N)  SPACE: O(N)

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Bucket sort approach — O(N) time."""
    count = Counter(nums)
    # Bucket: index = frequency, value = list of numbers with that freq
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)
    
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    return result


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())


# ============================================================
# TEMPLATE 3: Prefix Sum
# ============================================================
# USE WHEN: "Subarray sum", "range sum query", "cumulative"
# TIME: O(N) build, O(1) per query  SPACE: O(N)

def build_prefix_sum(nums: List[int]) -> List[int]:
    """prefix[i] = sum(nums[0:i]). Sum of nums[i:j] = prefix[j] - prefix[i]."""
    return [0] + list(accumulate(nums))


def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """Count subarrays summing to k. Prefix sum + hash map."""
    prefix_count = {0: 1}
    curr_sum = result = 0
    for num in nums:
        curr_sum += num
        result += prefix_count.get(curr_sum - k, 0)
        prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1
    return result


def product_except_self(nums: List[int]) -> List[int]:
    """Product of array except self — no division allowed.
    Build prefix product from left, then multiply suffix from right."""
    n = len(nums)
    result = [1] * n
    # Left pass: result[i] = product of all nums[0..i-1]
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    # Right pass: multiply by product of all nums[i+1..n-1]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result


# ============================================================
# TEMPLATE 4: Set for Existence / Uniqueness
# ============================================================

def contains_duplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))


def longest_consecutive_sequence(nums: List[int]) -> int:
    """O(N) using set. Only start counting from sequence starts."""
    num_set = set(nums)
    longest = 0
    for num in num_set:
        # Only process if num is the START of a sequence
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert top_k_frequent([1,1,1,2,2,3], 2) == [1, 2]
    assert is_anagram("anagram", "nagaram") == True
    assert subarray_sum_equals_k([1,1,1], 2) == 2
    assert product_except_self([1,2,3,4]) == [24,12,8,6]
    assert longest_consecutive_sequence([100,4,200,1,3,2]) == 4
    print("✅ All arrays & hashing templates passed!")
