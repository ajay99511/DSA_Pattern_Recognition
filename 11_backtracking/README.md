# Backtracking

## 🎯 When to Use
**Signal words**: "generate all", "find all", "permutations", "combinations", "subsets", "N-queens", "palindrome partitioning"

## 🧠 Core Concept
Explore all possibilities using DFS. At each step: **choose → explore → unchoose (backtrack)**.

## 📐 The Universal Backtracking Template
```python
def backtrack(candidates, path, result, start):
    if GOAL_REACHED:
        result.append(path[:])  # Always copy!
        return
    for i in range(start, len(candidates)):
        if SHOULD_SKIP: continue
        path.append(candidates[i])       # Choose
        backtrack(candidates, path, result, i + 1)  # Explore
        path.pop()                        # Unchoose
```

## Three Variants
| Variant | `start` parameter | Duplicates in result? |
|---------|-------------------|----------------------|
| Subsets | `i + 1` (no reuse) | Sort + skip `if i > start and nums[i] == nums[i-1]` |
| Permutations | Always 0, use `visited` set | Skip if `visited[i]` |
| Combinations w/ reuse | `i` (allow reuse) | No skip needed |

## 🏋️ Practice Problems
| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #78 Subsets | Medium | Include/exclude each element |
| 2 | LC #39 Combination Sum | Medium | Unlimited reuse → start=i |
| 3 | LC #40 Combination Sum II | Medium | No reuse + skip duplicates |
| 4 | LC #46 Permutations | Medium | Use visited array |
| 5 | LC #131 Palindrome Partitioning | Medium | Backtrack with palindrome check |
| 6 | LC #79 Word Search | Medium | Grid DFS backtracking |
| 7 | LC #51 N-Queens | Hard | Place queen per row, validate |
| 8 | LC #17 Letter Combinations Phone | Medium | Map digits → letters, backtrack |
