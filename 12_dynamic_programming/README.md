# Dynamic Programming — Deep Dive

## 🎯 When to Use
**Signal words**: "minimum cost", "maximum profit", "number of ways", "can you reach", "longest/shortest", "count paths", "optimal"

**Confirmation test**: Does the problem have **overlapping subproblems** AND **optimal substructure**?

## 🧠 The DP Process (ALWAYS follow this)
1. Define the **state**: What does `dp[i]` (or `dp[i][j]`) represent?
2. Write the **recurrence**: How does `dp[i]` relate to previous states?
3. Define the **base case**: What are the trivial values?
4. Determine the **iteration order**: Bottom-up filling direction.
5. Optimize **space** if possible: Can you use rolling variables?

## 📐 Six Sub-Pattern Templates

### Sub-Pattern 1: 1D Linear DP
```python
# dp[i] = best answer considering first i elements
def climb_stairs(n):
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b
```

### Sub-Pattern 2: 2D Grid/String DP
```python
# dp[i][j] = answer for s1[:i] and s2[:j]
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = i
    for j in range(n+1): dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
```

### Sub-Pattern 3: Knapsack
```python
# 0/1 Knapsack: dp[i][w] = max value using first i items with capacity w
# Unbounded: dp[w] = max value with capacity w (iterate items inside)
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

### Sub-Pattern 4: Interval DP
```python
# dp[i][j] = best answer for subarray nums[i..j]
# Try every split point k between i and j
def burst_balloons(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]
    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
    return dp[0][n-1]
```

### Sub-Pattern 5: State Machine DP
```python
# Multiple states tracking (hold/not_hold/cooldown)
def max_profit_cooldown(prices):
    hold, sold, rest = float('-inf'), 0, 0
    for p in prices:
        prev_hold = hold
        hold = max(hold, rest - p)
        rest = max(rest, sold)
        sold = prev_hold + p
    return max(sold, rest)
```

### Sub-Pattern 6: LIS (Longest Increasing Subsequence)
```python
from bisect import bisect_left
def lis(nums):
    tails = []
    for num in nums:
        pos = bisect_left(tails, num)
        if pos == len(tails): tails.append(num)
        else: tails[pos] = num
    return len(tails)  # O(N log N)
```

## 🏋️ Practice Problems (25 problems)

### 1D DP
| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #70 Climbing Stairs | Easy | dp[i] = dp[i-1] + dp[i-2] |
| 2 | LC #198 House Robber | Medium | dp[i] = max(dp[i-1], dp[i-2]+nums[i]) |
| 3 | LC #213 House Robber II | Medium | Circular: max(rob[0..n-2], rob[1..n-1]) |
| 4 | LC #91 Decode Ways | Medium | dp[i] depends on 1-digit and 2-digit checks |
| 5 | LC #139 Word Break | Medium | dp[i] = any(dp[j] and s[j:i] in dict) |

### 2D DP
| 6 | LC #62 Unique Paths | Medium | dp[r][c] = dp[r-1][c] + dp[r][c-1] |
| 7 | LC #64 Minimum Path Sum | Medium | dp[r][c] = grid[r][c] + min(up, left) |
| 8 | LC #72 Edit Distance | Medium | Classic 2D string DP |
| 9 | LC #1143 LCS | Medium | dp[i][j] = match vs max(skip) |
| 10 | LC #97 Interleaving String | Medium | dp[i][j] = can form s3[:i+j] from s1[:i]+s2[:j] |

### Knapsack
| 11 | LC #322 Coin Change | Medium | Unbounded knapsack |
| 12 | LC #518 Coin Change 2 | Medium | Count ways (order doesn't matter) |
| 13 | LC #416 Partition Equal Subset | Medium | 0/1 knapsack: can sum to total/2? |
| 14 | LC #494 Target Sum | Medium | Transform to subset sum |

### Interval DP & LIS
| 15 | LC #300 LIS | Medium | Patience sorting O(N log N) |
| 16 | LC #312 Burst Balloons | Hard | dp[i][j] = best for range |
| 17 | LC #131 Palindrome Partition | Medium | DP precompute + backtrack |

### State Machine DP
| 18 | LC #121 Best Time Buy/Sell | Easy | Track min price, max profit |
| 19 | LC #122 Buy/Sell II | Medium | Buy/sell multiple times |
| 20 | LC #309 Buy/Sell Cooldown | Medium | hold/sold/rest states |
| 21 | LC #188 Buy/Sell IV | Hard | K transactions → 2K states |

### Hard DP
| 22 | LC #152 Max Product Subarray | Medium | Track max AND min (negatives flip) |
| 23 | LC #10 Regular Expression Match | Hard | dp[i][j] = does s[:i] match p[:j] |
| 24 | LC #329 Longest Increasing Path | Hard | DFS + memoization on grid |
| 25 | LC #115 Distinct Subsequences | Hard | dp[i][j] = ways to form t[:j] from s[:i] |
