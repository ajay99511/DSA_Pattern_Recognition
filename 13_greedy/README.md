# Greedy

## 🎯 When to Use
**Signal words**: "maximum/minimum with constraint", "schedule", "jump game", "assign", "partition", "gas station"

**Key test**: Can a LOCAL optimal choice lead to GLOBAL optimal? If yes → Greedy. If no → DP.

## 📐 Core Approach
1. Sort by some criterion (start time, end time, ratio, etc.)
2. Process greedily: always pick the locally best option
3. Prove correctness: "exchange argument" — swapping any other choice can't improve result

## 🏋️ Practice Problems
| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #53 Maximum Subarray | Medium | Kadane's: reset if sum < 0 |
| 2 | LC #55 Jump Game | Medium | Track farthest reachable |
| 3 | LC #45 Jump Game II | Medium | BFS-like: count level jumps |
| 4 | LC #134 Gas Station | Medium | If total gas ≥ total cost, solution exists |
| 5 | LC #846 Hand of Straights | Medium | Sort + greedily build groups |
| 6 | LC #763 Partition Labels | Medium | Track last occurrence, extend partition |
| 7 | LC #678 Valid Parenthesis String | Medium | Track lo/hi range of open parens |
