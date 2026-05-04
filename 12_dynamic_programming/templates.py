"""Dynamic Programming — Reusable Templates"""
from typing import List
from functools import lru_cache
from bisect import bisect_left


# ============================================================
# 1D DP
# ============================================================

def climb_stairs(n: int) -> int:
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def house_robber(nums: List[int]) -> int:
    if not nums: return 0
    if len(nums) <= 2: return max(nums)
    a, b = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        a, b = b, max(b, a + nums[i])
    return b


def word_break(s: str, wordDict: List[str]) -> bool:
    words = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[-1]


# ============================================================
# 2D DP
# ============================================================

def unique_paths(m: int, n: int) -> int:
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]


def edit_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]


def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


# ============================================================
# KNAPSACK
# ============================================================

def coin_change(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


def can_partition(nums: List[int]) -> bool:
    """LC #416 — Partition Equal Subset Sum (0/1 Knapsack)."""
    total = sum(nums)
    if total % 2: return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):  # Reverse for 0/1
            dp[j] = dp[j] or dp[j - num]
    return dp[target]


# ============================================================
# STATE MACHINE DP
# ============================================================

def max_profit_cooldown(prices: List[int]) -> int:
    """LC #309 — States: hold, sold, rest."""
    hold, sold, rest = float('-inf'), 0, 0
    for p in prices:
        prev_hold = hold
        hold = max(hold, rest - p)
        rest = max(rest, sold)
        sold = prev_hold + p
    return max(sold, rest)


# ============================================================
# LIS — O(N log N)
# ============================================================

def length_of_lis(nums: List[int]) -> int:
    """LC #300 — Patience sorting approach."""
    tails = []
    for num in nums:
        pos = bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)


# ============================================================
# MAX PRODUCT SUBARRAY
# ============================================================

def max_product(nums: List[int]) -> int:
    """LC #152 — Track both max and min (negatives flip)."""
    result = cur_max = cur_min = nums[0]
    for num in nums[1:]:
        if num < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(num, cur_max * num)
        cur_min = min(num, cur_min * num)
        result = max(result, cur_max)
    return result


if __name__ == "__main__":
    assert climb_stairs(5) == 8
    assert house_robber([2,7,9,3,1]) == 12
    assert word_break("leetcode", ["leet","code"]) == True
    assert unique_paths(3, 7) == 28
    assert edit_distance("horse", "ros") == 3
    assert longest_common_subsequence("abcde", "ace") == 3
    assert coin_change([1,5,11], 15) == 3
    assert can_partition([1,5,11,5]) == True
    assert length_of_lis([10,9,2,5,3,7,101,18]) == 4
    assert max_product([2,3,-2,4]) == 6
    print("✅ All DP templates passed!")
