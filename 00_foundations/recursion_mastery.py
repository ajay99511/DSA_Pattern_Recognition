"""
🔄 Recursion Mastery
====================
Foundation for: Trees, Graphs, Backtracking, DP.

KEY INSIGHT: Don't trace the full recursion tree.
Trust the recursive call works, and focus on:
  1. What's the BASE CASE?
  2. What's the RECURSIVE STEP?
  3. What does each call RETURN?
"""

from functools import lru_cache
from typing import List, Optional


# ============================================================
# THE "LEAP OF FAITH" — The Only Way to Think About Recursion
# ============================================================
# When writing recursion, ASSUME the recursive call works correctly.
# Example: "Sum of a list"
#   IF sum(rest) correctly sums everything except first,
#   THEN answer = first + sum(rest)

def recursive_sum(arr: List[int]) -> int:
    if not arr:
        return 0
    return arr[0] + recursive_sum(arr[1:])


# ============================================================
# THE 5 RECURSION PATTERNS
# ============================================================

# PATTERN 1: LINEAR — process one element, recurse on rest
def factorial(n: int) -> int:
    if n <= 1: return 1
    return n * factorial(n - 1)

def reverse_string(s: str) -> str:
    if len(s) <= 1: return s
    return s[-1] + reverse_string(s[:-1])


# PATTERN 2: BINARY — split into two halves
def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# PATTERN 3: TREE — process node, recurse on children
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def max_depth(root: Optional[TreeNode]) -> int:
    """TRUST: max_depth(child) returns correct depth.
    THEN: this node's depth = 1 + max(left_depth, right_depth)."""
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root: return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root


# PATTERN 4: BACKTRACKING — try choices, undo if wrong
def generate_subsets(nums: List[int]) -> List[List[int]]:
    result = []
    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])  # Copy!
            return
        current.append(nums[index])      # Include
        backtrack(index + 1, current)
        current.pop()                    # BACKTRACK (exclude)
        backtrack(index + 1, current)
    backtrack(0, [])
    return result


# PATTERN 5: DIVIDE AND CONQUER — split, solve, combine
def find_max(arr, lo, hi):
    if lo == hi: return arr[lo]
    mid = (lo + hi) // 2
    return max(find_max(arr, lo, mid), find_max(arr, mid + 1, hi))


# ============================================================
# RECURSION → DP PIPELINE (The Most Important Skill)
# ============================================================
# Every DP problem: Recursion → Add memo → Convert to iteration

# Step 1: Pure recursion — O(2^N) exponential
def fib_recursive(n):
    if n <= 1: return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Step 2: Add memoization — O(N) top-down DP
@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1: return n
    return fib_memo(n-1) + fib_memo(n-2)

# Step 3: Bottom-up iteration — O(N) time, O(1) space
def fib_bottom_up(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b


# ============================================================
# RECURSION DEBUGGING CHECKLIST
# ============================================================
"""
When your recursive solution is WRONG, check:
1. □ BASE CASE — Does it handle smallest input? Return correct value?
2. □ PROGRESS — Does each call move toward base case?
3. □ COMBINING — Using recursive results correctly? (max vs sum vs +1)
4. □ STATE — Mutable state (lists): Did you BACKTRACK?
5. □ RETURN — Every path returns consistently?
"""

# ============================================================
# WHEN TO USE ITERATIVE vs RECURSIVE
# ============================================================
"""
N ≤ 1000:  Recursion fine (Python default stack)
N > 1000:  Iterative OR sys.setrecursionlimit(10**6)
Trees:     Recursion usually cleaner
Graphs:    Iterative safer (avoid stack overflow)
DP:        Bottom-up (iterative) faster in practice
"""

def dfs_iterative(graph, start):
    """DFS with explicit stack — handles any depth."""
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node in visited: continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return visited


if __name__ == "__main__":
    assert recursive_sum([1,2,3,4,5]) == 15
    assert factorial(5) == 120
    assert reverse_string("hello") == "olleh"
    assert merge_sort([5,3,1,4,2]) == [1,2,3,4,5]
    assert fib_memo(10) == 55
    assert fib_bottom_up(10) == 55
    assert len(generate_subsets([1,2,3])) == 8
    print("✅ All recursion tests passed!")
