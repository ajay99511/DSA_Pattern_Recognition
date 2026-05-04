# Binary Search

## 🎯 When to Use This Pattern
**Signal words**: "sorted", "minimum/maximum that satisfies", "find boundary", "search in rotated", "find peak"

**Key insight**: Binary search works whenever the **search space is monotonic** — there's a clear boundary between "yes" and "no" answers.

## 📐 Templates

### Template 1: Classic Binary Search
```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target: return mid
        elif nums[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1
```

### Template 2: Find Left Boundary (First occurrence ≥ target)
```python
def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target: lo = mid + 1
        else: hi = mid
    return lo  # First index where nums[i] >= target
```

### Template 3: Binary Search on Answer
```python
def min_days_to_make_bouquets(bloomDay, m, k):
    def can_make(days):
        bouquets = flowers = 0
        for bloom in bloomDay:
            if bloom <= days: flowers += 1
            else: flowers = 0
            if flowers == k: bouquets += 1; flowers = 0
        return bouquets >= m
    lo, hi = min(bloomDay), max(bloomDay)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_make(mid): hi = mid
        else: lo = mid + 1
    return lo
```

## 🏋️ Practice Problems
| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #704 Binary Search | Easy | Classic template |
| 2 | LC #33 Search in Rotated Sorted | Medium | Find sorted half, decide which to search |
| 3 | LC #153 Find Min in Rotated Sorted | Medium | Compare mid with right boundary |
| 4 | LC #875 Koko Eating Bananas | Medium | Binary search on answer (eating speed) |
| 5 | LC #74 Search 2D Matrix | Medium | Flatten 2D → 1D index mapping |
| 6 | LC #981 Time Based Key-Value Store | Medium | Binary search on timestamps |
| 7 | LC #4 Median of Two Sorted Arrays | Hard | Binary search on partition point |
| 8 | LC #410 Split Array Largest Sum | Hard | Binary search on answer + greedy check |
