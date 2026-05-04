# Arrays & Hashing

## 🎯 When to Use This Pattern

**Signal words**: "find pair", "group", "count occurrences", "frequency", "duplicate", "anagram", "subarray sum equals K", "two sum"

**Input characteristics**:
- Unsorted array where you need O(1) lookups
- Need to count/track frequencies
- Need to find pairs or groups matching a condition
- Cumulative/running aggregates over subarrays

## 🧠 Core Concept

Hash maps give you **O(1) average** lookup/insert/delete. This turns O(N²) brute force (check every pair) into O(N) (check hash map for complement).

Three sub-patterns:
1. **Hash Map for Complement Lookup** — "Does the thing I need exist?" (Two Sum)
2. **Frequency Counting** — "How many of each?" (Anagram, Top K)
3. **Prefix Sum** — "Sum of subarray [i..j]?" → `prefix[j+1] - prefix[i]`

## 📐 Templates

### Template 1: Complement Lookup (Two Sum pattern)
```python
def two_sum(nums, target):
    seen = {}  # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

### Template 2: Frequency Counting
```python
from collections import Counter
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))  # Canonical form
        groups[key].append(s)
    return list(groups.values())
```

### Template 3: Prefix Sum
```python
from itertools import accumulate
def subarray_sum_equals_k(nums, k):
    prefix_count = {0: 1}  # prefix_sum → count of occurrences
    curr_sum, result = 0, 0
    for num in nums:
        curr_sum += num
        # If (curr_sum - k) exists as a previous prefix, we found a subarray
        result += prefix_count.get(curr_sum - k, 0)
        prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1
    return result
```

## ⚡ Variations

| Variation | Key Difference | Example |
|-----------|---------------|---------|
| Value → Index mapping | Store index in hash | Two Sum |
| Frequency map | Count occurrences | Top K Frequent |
| Canonical form grouping | Transform to hashable key | Group Anagrams |
| Prefix sum + hash | Cumulative sum lookups | Subarray Sum = K |
| Set for existence | Just need True/False | Contains Duplicate |

## 🏋️ Practice Problems

| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #217 Contains Duplicate | Easy | Set — O(1) existence check |
| 2 | LC #242 Valid Anagram | Easy | Counter comparison |
| 3 | LC #1 Two Sum | Easy | Hash map complement lookup |
| 4 | LC #49 Group Anagrams | Medium | Sorted tuple as hash key |
| 5 | LC #347 Top K Frequent | Medium | Counter + heap (or bucket sort) |
| 6 | LC #238 Product of Array Except Self | Medium | Prefix + suffix products |
| 7 | LC #560 Subarray Sum Equals K | Medium | Prefix sum + hash map |
| 8 | LC #128 Longest Consecutive Sequence | Medium | Set + expand from start of sequence |
| 9 | LC #36 Valid Sudoku | Medium | Sets for row/col/box tracking |
| 10 | LC #271 Encode/Decode Strings | Medium | Length-prefix encoding |
| 11 | LC #41 First Missing Positive | Hard | Use array itself as hash map (index marking) |

## 🔗 Related Patterns
- **Two Pointers**: When array is sorted, two pointers often replaces hash map
- **Sliding Window**: For contiguous subarray problems with hash map tracking
- **Prefix Sum**: Often combined with hash map for subarray sum queries
