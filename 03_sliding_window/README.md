# Sliding Window

## 🎯 When to Use This Pattern

**Signal words**: "contiguous subarray", "substring", "window", "maximum/minimum of size K", "at most K distinct", "longest/shortest"

**Input**: Array or string where you need to find an optimal contiguous subsequence.

## 🧠 Core Concept

Maintain a "window" [left, right] that expands and contracts. Avoid recomputing from scratch — instead, **add the new element** and **remove the old element** incrementally.

Two sub-patterns:
1. **Fixed Window** — Window size is given (K). Slide it across.
2. **Variable Window** — Expand right to explore, shrink left when constraint violated.

## 📐 Templates

### Template 1: Fixed Window
```python
def max_sum_subarray_k(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]  # Add new, remove old
        max_sum = max(max_sum, window_sum)
    return max_sum
```

### Template 2: Variable Window (Expand/Shrink)
```python
def longest_substring_k_distinct(s, k):
    freq = {}
    left = max_len = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1  # Expand
        while len(freq) > k:                          # Constraint violated
            freq[s[left]] -= 1                         # Shrink
            if freq[s[left]] == 0: del freq[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)       # Update answer
    return max_len
```

### Template 3: Minimum Window (Shrink to optimize)
```python
def min_window_substring(s, t):
    from collections import Counter
    need = Counter(t)
    missing = len(t)
    left = start = 0
    min_len = float('inf')
    for right, char in enumerate(s):
        if need[char] > 0: missing -= 1
        need[char] -= 1
        while missing == 0:  # All chars found → try to shrink
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left
            need[s[left]] += 1
            if need[s[left]] > 0: missing += 1
            left += 1
    return s[start:start+min_len] if min_len != float('inf') else ""
```

## 🏋️ Practice Problems

| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #643 Max Avg Subarray I | Easy | Fixed window of size K |
| 2 | LC #3 Longest Substring No Repeat | Medium | Variable window + set/hashmap |
| 3 | LC #424 Longest Repeating Char Replacement | Medium | Window valid if (len - max_freq) ≤ k |
| 4 | LC #567 Permutation in String | Medium | Fixed window + frequency match |
| 5 | LC #76 Minimum Window Substring | Hard | Shrink after all chars found |
| 6 | LC #239 Sliding Window Maximum | Hard | Monotonic deque for O(N) |
| 7 | LC #438 Find All Anagrams | Medium | Fixed window + Counter comparison |

## 🔗 Related Patterns
- **Two Pointers**: Sliding window IS two pointers with a window between them
- **Hash Map**: Often used inside the window to track frequencies
- **Monotonic Deque**: Used for "sliding window maximum/minimum" problems
