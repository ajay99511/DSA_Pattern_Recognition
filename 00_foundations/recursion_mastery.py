"""
🔄 Recursion Mastery
====================
Foundation for: Trees, Graphs, Backtracking, DP.

KEY INSIGHT: Don't trace the full recursion tree.
Trust the recursive call works, and focus on:
  1. What's the BASE CASE?
  2. What's the RECURSIVE STEP?
  3. What does each call RETURN?

CONTENTS:
  - The "Leap of Faith" mental model
  - Pattern 1: LINEAR recursion
  - Pattern 2: BINARY recursion
  - Pattern 3: TREE recursion
  - Pattern 4: BACKTRACKING
  - Pattern 5: DIVIDE AND CONQUER
  - Recursion → DP Pipeline (pure → memo → bottom-up)
  - Recursion Debugging Checklist
  - When to use Iterative vs Recursive
"""

from functools import lru_cache
from typing import List, Optional, Tuple


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

# ─────────────────────────────────────────────────────────────
# PATTERN 1: LINEAR — process one element, recurse on rest
# ─────────────────────────────────────────────────────────────
# Shape:  f(n) = work(n) + f(n-1)
# Depth:  O(N)   |   Stack frames: O(N)
# When:   Linked lists, arrays processed one-by-one, countdown
#
# RECOGNITION SIGNALS:
#   - "process each element one at a time"
#   - "linked list traversal / reversal"
#   - "accumulate a result across all elements"

def factorial(n: int) -> int:
    """Classic linear recursion: n! = n * (n-1)!"""
    if n <= 1: return 1
    return n * factorial(n - 1)

def reverse_string(s: str) -> str:
    """Reverse by taking last char + reverse of rest."""
    if len(s) <= 1: return s
    return s[-1] + reverse_string(s[:-1])

# INTERVIEW-RELEVANT: Linked list reversal (linear recursion on nodes)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    TRUST: reverse_linked_list(head.next) correctly reverses the rest.
    THEN:  attach head at the end of the reversed sublist.
    Time: O(N)  Space: O(N) stack — use iterative for N > 1000
    """
    if not head or not head.next:
        return head
    new_head = reverse_linked_list(head.next)  # reverse rest
    head.next.next = head   # point next node back to head
    head.next = None        # cut old forward link
    return new_head

def sum_to_n(n: int) -> int:
    """Sum 1..n — shows linear accumulation pattern."""
    if n == 0: return 0
    return n + sum_to_n(n - 1)


# ─────────────────────────────────────────────────────────────
# PATTERN 2: BINARY — split into two halves (merge sort style)
# ─────────────────────────────────────────────────────────────
# Shape:  f(n) = combine(f(n/2), f(n/2))
# Depth:  O(log N)   |   Stack frames: O(log N)
# When:   Sorting, searching, "split and conquer on equal halves"
#
# RECOGNITION SIGNALS:
#   - "sort / merge"
#   - "find in sorted array"
#   - "balanced split gives efficiency"

def merge_sort(arr: List[int]) -> List[int]:
    """
    Split → sort each half → merge.
    Time: O(N log N)  Space: O(N) for merge buffer + O(log N) stack
    """
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # Merge step — O(N)
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def binary_search_recursive(arr: List[int], target: int, lo: int, hi: int) -> int:
    """
    Binary recursion on a sorted array — classic O(log N) search.
    Returns index of target, or -1 if not found.
    """
    if lo > hi: return -1
    mid = (lo + hi) // 2
    if arr[mid] == target: return mid
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, hi)
    return binary_search_recursive(arr, target, lo, mid - 1)


# ─────────────────────────────────────────────────────────────
# PATTERN 3: TREE — process node, recurse on children
# ─────────────────────────────────────────────────────────────
# Shape:  f(node) = work(node) + f(node.left) + f(node.right)
# Depth:  O(H) where H = tree height (O(log N) balanced, O(N) skewed)
# When:   Any binary tree problem — depth, paths, subtree checks
#
# RECOGNITION SIGNALS:
#   - "binary tree" in problem
#   - "path from root to leaf"
#   - "subtree property" (symmetric, same tree, etc.)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def max_depth(root: Optional[TreeNode]) -> int:
    """
    TRUST: max_depth(child) returns correct depth of subtree.
    THEN:  this node's depth = 1 + max(left_depth, right_depth).
    Time: O(N)  Space: O(H)
    """
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Mirror a binary tree. Time: O(N)  Space: O(H)"""
    if not root: return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root

def has_path_sum(root: Optional[TreeNode], target: int) -> bool:
    """
    INTERVIEW CLASSIC: Does any root-to-leaf path sum to target?
    TRUST: has_path_sum(child, target - root.val) answers for subtree.
    Time: O(N)  Space: O(H)
    """
    if not root: return False
    if not root.left and not root.right:   # leaf node
        return root.val == target
    remaining = target - root.val
    return has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining)

def lowest_common_ancestor(root: Optional[TreeNode],
                           p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    INTERVIEW CLASSIC: LCA of two nodes in a BST-agnostic tree.
    Key insight: if both p and q found in different subtrees → current node is LCA.
    Time: O(N)  Space: O(H)
    """
    if not root or root == p or root == q:
        return root
    left  = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right: return root   # p in left subtree, q in right
    return left if left else right   # both in same subtree


# ─────────────────────────────────────────────────────────────
# PATTERN 4: BACKTRACKING — try choices, undo if wrong
# ─────────────────────────────────────────────────────────────
# Shape:  for choice in choices: make → recurse → UNDO
# Depth:  O(N)   |   Total calls: O(2^N) subsets, O(N!) perms
# When:   "all combinations/permutations/subsets", constraint satisfaction
#
# RECOGNITION SIGNALS:
#   - "generate all ..."
#   - "find all valid ..."
#   - "N-Queens, Sudoku, word search"
#
# TEMPLATE:
#   def backtrack(state):
#       if is_complete(state): record(); return
#       for choice in get_choices(state):
#           make_choice(choice)
#           backtrack(state)
#           undo_choice(choice)   ← THE KEY STEP

def generate_subsets(nums: List[int]) -> List[List[int]]:
    """
    All 2^N subsets. Each element: include or exclude.
    Time: O(N * 2^N)  Space: O(N) stack + O(2^N) output
    """
    result = []
    def backtrack(index: int, current: List[int]) -> None:
        if index == len(nums):
            result.append(current[:])  # snapshot — must copy!
            return
        # Choice 1: include nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()                  # UNDO — backtrack

        # Choice 2: exclude nums[index]
        backtrack(index + 1, current)
    backtrack(0, [])
    return result

def generate_permutations(nums: List[int]) -> List[List[int]]:
    """
    All N! permutations. Each position: pick any unused element.
    Time: O(N * N!)  Space: O(N) stack + O(N!) output
    """
    result = []
    used = [False] * len(nums)

    def backtrack(current: List[int]) -> None:
        if len(current) == len(nums):
            result.append(current[:])  # snapshot
            return
        for i, num in enumerate(nums):
            if used[i]: continue
            used[i] = True             # make choice
            current.append(num)
            backtrack(current)
            current.pop()              # UNDO
            used[i] = False            # UNDO

    backtrack([])
    return result

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    INTERVIEW CLASSIC: All combos that sum to target (reuse allowed).
    Prune: skip if remaining < 0 (no point going deeper).
    Time: O(N^(T/M)) where T=target, M=min candidate
    """
    result = []
    candidates.sort()  # enables early pruning

    def backtrack(start: int, current: List[int], remaining: int) -> None:
        if remaining == 0:
            result.append(current[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining: break  # pruning
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # reuse allowed
            current.pop()

    backtrack(0, [], target)
    return result


# ─────────────────────────────────────────────────────────────
# PATTERN 5: DIVIDE AND CONQUER — split, solve, combine
# ─────────────────────────────────────────────────────────────
# Shape:  f(problem) = combine(f(left_half), f(right_half))
# Depth:  O(log N)   |   Total work: depends on combine step
# When:   "find kth element", "closest pair", "matrix multiply"
#
# DIFFERENCE FROM BINARY RECURSION:
#   Binary recursion (Pattern 2): both halves are equal-sized, combine is merge
#   D&C (Pattern 5): halves may be unequal, combine logic is the key insight
#
# RECOGNITION SIGNALS:
#   - "kth largest/smallest" (QuickSelect)
#   - "count inversions"
#   - "maximum subarray" (Kadane's has iterative form, but D&C is O(N log N))

def find_max(arr: List[int], lo: int, hi: int) -> int:
    """Simple D&C max — illustrates the split/combine skeleton."""
    if lo == hi: return arr[lo]
    mid = (lo + hi) // 2
    return max(find_max(arr, lo, mid), find_max(arr, mid + 1, hi))

def quick_select(arr: List[int], lo: int, hi: int, k: int) -> int:
    """
    INTERVIEW CLASSIC: Find kth smallest element in O(N) average.
    D&C: partition around pivot, recurse only on relevant half.
    Time: O(N) average, O(N^2) worst  Space: O(log N) stack
    """
    if lo == hi: return arr[lo]

    # Partition step — Lomuto scheme
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    pivot_idx = i

    if k == pivot_idx:
        return arr[pivot_idx]
    elif k < pivot_idx:
        return quick_select(arr, lo, pivot_idx - 1, k)
    else:
        return quick_select(arr, pivot_idx + 1, hi, k)

def power(base: float, exp: int) -> float:
    """
    Fast exponentiation via D&C: x^n = x^(n/2) * x^(n/2).
    Time: O(log N)  — much better than O(N) naive multiply.
    """
    if exp == 0: return 1.0
    if exp < 0: return 1.0 / power(base, -exp)
    half = power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return base * half * half


# ============================================================
# RECURSION → DP PIPELINE (The Most Important Skill)
# ============================================================
# Every DP problem follows this exact pipeline:
#   1. Pure recursion  → identify overlapping subproblems
#   2. Memoization     → cache results (top-down DP)
#   3. Bottom-up table → eliminate recursion entirely
#
# WHEN TO STOP:
#   - Memoization is fine for interviews (simpler to write)
#   - Bottom-up is better for space optimization (rolling array)
#   - Bottom-up avoids Python's recursion limit

# ── EXAMPLE A: Fibonacci (simplest pipeline demo) ──────────

# Step 1: Pure recursion — O(2^N) exponential (overlapping subproblems!)
def fib_recursive(n: int) -> int:
    if n <= 1: return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Step 2: Add memoization — O(N) time, O(N) space (top-down DP)
@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    if n <= 1: return n
    return fib_memo(n-1) + fib_memo(n-2)

# Step 3: Bottom-up iteration — O(N) time, O(1) space
def fib_bottom_up(n: int) -> int:
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# ── EXAMPLE B: Coin Change (real interview DP pipeline) ────
# Problem: minimum coins to make amount (coins can repeat)

# Step 1: Pure recursion — exponential, TLE
def coin_change_recursive(coins: List[int], amount: int) -> int:
    if amount == 0: return 0
    if amount < 0:  return float('inf')
    return 1 + min(coin_change_recursive(coins, amount - c) for c in coins)

# Step 2: Memoization — O(N * amount) top-down DP
def coin_change_memo(coins: List[int], amount: int) -> int:
    memo = {}
    def dp(remaining: int) -> int:
        if remaining == 0: return 0
        if remaining < 0:  return float('inf')
        if remaining in memo: return memo[remaining]
        memo[remaining] = 1 + min(dp(remaining - c) for c in coins)
        return memo[remaining]
    result = dp(amount)
    return result if result != float('inf') else -1

# Step 3: Bottom-up — O(N * amount) time, O(amount) space
def coin_change_bottom_up(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != float('inf') else -1

# ── PIPELINE DECISION GUIDE ────────────────────────────────
# Q: Does the problem have OPTIMAL SUBSTRUCTURE?
#    (optimal solution built from optimal sub-solutions)
#    → YES: DP candidate
# Q: Are there OVERLAPPING SUBPROBLEMS?
#    (same sub-problem solved multiple times in recursion tree)
#    → YES: Add memoization
# Q: Need O(1) space or avoid recursion limit?
#    → Convert to bottom-up with rolling array


# ============================================================
# RECURSION DEBUGGING CHECKLIST
# ============================================================
"""
When your recursive solution is WRONG, check in order:

□ 1. BASE CASE
     - Does it handle the SMALLEST valid input?
     - Does it return the CORRECT value (not just stop)?
     - Are there MULTIPLE base cases you're missing?
     BAD:  if n == 0: return   ← returns None, not 0
     GOOD: if n == 0: return 0

□ 2. PROGRESS (Convergence)
     - Does EVERY recursive call move toward the base case?
     - Can you get into an infinite loop?
     BAD:  return f(n)         ← same n, infinite loop
     GOOD: return f(n - 1)     ← strictly smaller

□ 3. COMBINING (Trust the recursion)
     - Are you using the recursive result CORRECTLY?
     - max vs sum vs +1 — which operation is right?
     BAD:  return max_depth(root.left)          ← ignores right
     GOOD: return 1 + max(max_depth(root.left),
                          max_depth(root.right))

□ 4. STATE (Mutable data — backtracking)
     - Did you COPY mutable state before appending to results?
     - Did you UNDO every mutation after the recursive call?
     BAD:  result.append(current)   ← appends reference, mutates later
     GOOD: result.append(current[:])  ← snapshot copy
     BAD:  current.append(x); recurse()  ← no undo
     GOOD: current.append(x); recurse(); current.pop()

□ 5. RETURN VALUE (Consistency)
     - Does EVERY code path return a value?
     - Are return types consistent (int vs None vs list)?
     BAD:  if condition: return val  ← falls off end → returns None
     GOOD: if condition: return val
           return other_val

QUICK DIAGNOSIS FLOW:
  Wrong answer?  → Check #3 (combining logic)
  Infinite loop? → Check #2 (progress toward base case)
  None returned? → Check #1 (base case return value) or #5
  Mutated state? → Check #4 (copy + undo)
"""

# ============================================================
# WHEN TO USE ITERATIVE vs RECURSIVE
# ============================================================
"""
RULE OF THUMB:
  N ≤ 1000:   Recursion fine (Python default stack ~1000 frames)
  N > 1000:   Iterative OR sys.setrecursionlimit(10**6)
  Trees:      Recursion usually cleaner (height rarely > 50)
  Graphs:     Iterative safer (avoid stack overflow on large graphs)
  DP:         Bottom-up (iterative) faster in practice, avoids limit

COMPLEXITY COMPARISON:
  Pattern          | Recursive Stack | Iterative Stack
  ─────────────────┼─────────────────┼────────────────
  Linear (N)       | O(N)            | O(1)
  Binary (log N)   | O(log N)        | O(1)
  Tree (height H)  | O(H)            | O(H) explicit stack
  Backtracking     | O(N)            | O(N) explicit stack
  D&C              | O(log N)        | O(log N) explicit stack

INTERVIEW TIP: If interviewer asks "can you do it iteratively?",
  use an explicit stack to simulate the call stack.
"""

def dfs_iterative(graph: dict, start: int) -> set:
    """DFS with explicit stack — handles any depth, no recursion limit."""
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node in visited: continue
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                stack.append(neighbor)
    return visited

def bfs_iterative(graph: dict, start: int) -> List[int]:
    """BFS with deque — level-order traversal, shortest path in unweighted graph."""
    from collections import deque
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


if __name__ == "__main__":
    # ── Pattern 1: Linear ──────────────────────────────────
    assert recursive_sum([1,2,3,4,5]) == 15
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert reverse_string("hello") == "olleh"
    assert sum_to_n(10) == 55

    # Linked list reversal
    head = ListNode(1, ListNode(2, ListNode(3)))
    rev = reverse_linked_list(head)
    vals = []
    while rev: vals.append(rev.val); rev = rev.next
    assert vals == [3, 2, 1]

    # ── Pattern 2: Binary ──────────────────────────────────
    assert merge_sort([5,3,1,4,2]) == [1,2,3,4,5]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    arr = [1,3,5,7,9]
    assert binary_search_recursive(arr, 5, 0, len(arr)-1) == 2
    assert binary_search_recursive(arr, 6, 0, len(arr)-1) == -1

    # ── Pattern 3: Tree ────────────────────────────────────
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    assert max_depth(root) == 3
    assert max_depth(None) == 0

    path_root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                         TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    assert has_path_sum(path_root, 22) == True   # 5→4→11→2
    assert has_path_sum(path_root, 27) == True    # 5→4→11→7
    assert has_path_sum(path_root, 100) == False  # no such path

    # ── Pattern 4: Backtracking ────────────────────────────
    assert len(generate_subsets([1,2,3])) == 8
    assert len(generate_permutations([1,2,3])) == 6
    combos = combination_sum([2,3,6,7], 7)
    assert sorted([sorted(c) for c in combos]) == [[2,2,3],[7]]

    # ── Pattern 5: Divide & Conquer ────────────────────────
    assert find_max([3,1,4,1,5,9,2,6], 0, 7) == 9
    assert quick_select([3,1,4,1,5,9,2,6], 0, 7, 3) == 3  # 4th smallest (0-indexed)
    assert power(2.0, 10) == 1024.0
    assert abs(power(2.0, -2) - 0.25) < 1e-9

    # ── Recursion → DP Pipeline ────────────────────────────
    assert fib_memo(10) == 55
    assert fib_bottom_up(10) == 55
    assert fib_recursive(10) == 55
    assert coin_change_memo([1,5,11], 15) == 3    # 5+5+5
    assert coin_change_bottom_up([1,5,11], 15) == 3
    assert coin_change_bottom_up([2], 3) == -1    # impossible

    print("✅ All recursion tests passed!")
