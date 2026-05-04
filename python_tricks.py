"""
🐍 Python Tricks for Coding Interviews
=======================================
Master these idioms to write solutions 2x faster than other candidates.
Every trick here is interview-legal and commonly used in FAANG solutions.
"""

# ============================================================
# 1. ESSENTIAL IMPORTS — Memorize These
# ============================================================

from collections import defaultdict, Counter, deque, OrderedDict
from heapq import heappush, heappop, heapify, nlargest, nsmallest
from bisect import bisect_left, bisect_right, insort
from itertools import accumulate, combinations, permutations, product
from functools import lru_cache, reduce
from typing import List, Optional, Tuple, Dict, Set
from math import inf, gcd, ceil, floor, log2, sqrt, factorial
import string  # string.ascii_lowercase, string.digits

# ============================================================
# 2. HASH MAP / COUNTER TRICKS
# ============================================================

def hash_map_tricks():
    # --- defaultdict: Never check "if key in dict" again ---
    graph = defaultdict(list)
    graph['A'].append('B')  # No KeyError, auto-creates empty list
    
    freq = defaultdict(int)
    for x in [1, 2, 2, 3, 3, 3]:
        freq[x] += 1  # {1:1, 2:2, 3:3}
    
    # --- Counter: Frequency counting in one line ---
    text = "abracadabra"
    count = Counter(text)           # Counter({'a':5, 'b':2, 'r':2, 'c':1, 'd':1})
    count.most_common(2)            # [('a', 5), ('b', 2)]
    
    # Counter arithmetic (great for anagram checks)
    Counter("anagram") == Counter("nagaram")  # True
    Counter("abc") - Counter("ab")            # Counter({'c': 1})
    
    # --- Anagram grouping trick ---
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groups = defaultdict(list)
    for w in words:
        groups[tuple(sorted(w))].append(w)
    # {('a','e','t'): ['eat','tea','ate'], ('a','n','t'): ['tan','nat'], ...}


# ============================================================
# 3. HEAP TRICKS (Python only has MIN-HEAP)
# ============================================================

def heap_tricks():
    # --- Basic min-heap ---
    h = []
    heappush(h, 5)
    heappush(h, 1)
    heappush(h, 3)
    smallest = heappop(h)  # 1
    
    # --- MAX-HEAP: Negate the values ---
    max_h = []
    for val in [5, 1, 3]:
        heappush(max_h, -val)
    largest = -heappop(max_h)  # 5
    
    # --- Heap with tuples (for priority + data) ---
    tasks = []
    heappush(tasks, (2, "medium_task"))
    heappush(tasks, (1, "urgent_task"))
    heappush(tasks, (3, "low_task"))
    priority, task = heappop(tasks)  # (1, "urgent_task")
    
    # --- Heapify an existing list: O(N) instead of O(N log N) ---
    arr = [5, 3, 1, 4, 2]
    heapify(arr)  # In-place, now arr[0] is the minimum
    
    # --- Top K elements ---
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    top3 = nlargest(3, nums)   # [9, 6, 5]
    bot3 = nsmallest(3, nums)  # [1, 1, 2]


# ============================================================
# 4. BINARY SEARCH WITH BISECT
# ============================================================

def bisect_tricks():
    arr = [1, 3, 5, 5, 5, 7, 9]
    
    # --- Find insertion point (leftmost) ---
    bisect_left(arr, 5)    # 2 (first index where 5 can go)
    
    # --- Find insertion point (rightmost) ---
    bisect_right(arr, 5)   # 5 (after all existing 5s)
    
    # --- Count occurrences of value in sorted array ---
    count_5 = bisect_right(arr, 5) - bisect_left(arr, 5)  # 3
    
    # --- Insert while maintaining sort ---
    insort(arr, 4)  # arr = [1, 3, 4, 5, 5, 5, 7, 9]
    
    # --- "Find leftmost value >= target" (lower bound) ---
    def lower_bound(arr, target):
        idx = bisect_left(arr, target)
        return idx if idx < len(arr) else -1
    
    # --- "Find rightmost value <= target" (upper bound) ---
    def upper_bound(arr, target):
        idx = bisect_right(arr, target) - 1
        return idx if idx >= 0 else -1


# ============================================================
# 5. DEQUE TRICKS (for BFS, Sliding Window)
# ============================================================

def deque_tricks():
    # --- O(1) operations on both ends ---
    dq = deque()
    dq.append(1)       # [1]
    dq.appendleft(0)   # [0, 1]
    dq.pop()           # [0]      — removes from right
    dq.popleft()       # []       — removes from left (O(1)!)
    
    # --- BFS template with deque ---
    # queue = deque([(start, 0)])  # (node, distance)
    # while queue:
    #     node, dist = queue.popleft()
    #     for neighbor in graph[node]:
    #         queue.append((neighbor, dist + 1))
    
    # --- Fixed-size sliding window ---
    dq = deque(maxlen=3)
    for x in [1, 2, 3, 4, 5]:
        dq.append(x)
    # dq = deque([3, 4, 5], maxlen=3)  — auto-evicts old elements


# ============================================================
# 6. SORTING TRICKS
# ============================================================

def sorting_tricks():
    # --- Sort by custom key ---
    intervals = [(3, 5), (1, 3), (2, 8)]
    intervals.sort(key=lambda x: x[0])         # Sort by start
    intervals.sort(key=lambda x: x[1])         # Sort by end
    intervals.sort(key=lambda x: x[1] - x[0])  # Sort by length
    
    # --- Sort by multiple criteria ---
    students = [("Alice", 90), ("Bob", 85), ("Charlie", 90)]
    students.sort(key=lambda x: (-x[1], x[0]))  # Score desc, then name asc
    
    # --- Sort string characters ---
    s = "dcba"
    sorted_s = ''.join(sorted(s))  # "abcd"
    
    # --- Frequency sort ---
    nums = [1, 1, 2, 2, 2, 3]
    c = Counter(nums)
    nums.sort(key=lambda x: c[x], reverse=True)  # [2, 2, 2, 1, 1, 3]


# ============================================================
# 7. STRING TRICKS
# ============================================================

def string_tricks():
    # --- String → Char frequency ---
    Counter("hello")  # Counter({'l':2, 'h':1, 'e':1, 'o':1})
    
    # --- Check if string is all digits/alpha ---
    "123".isdigit()    # True
    "abc".isalpha()    # True
    "abc123".isalnum() # True
    
    # --- Reverse a string ---
    s = "hello"
    s[::-1]  # "olleh"
    
    # --- Join is faster than concatenation ---
    words = ["hello", "world"]
    ' '.join(words)    # "hello world"
    
    # --- Build string with list (O(N) instead of O(N²)) ---
    chars = []
    for c in "hello":
        chars.append(c.upper())
    result = ''.join(chars)  # "HELLO"
    
    # --- Check palindrome ---
    s = "racecar"
    s == s[::-1]  # True
    
    # --- ord/chr for character math ---
    ord('a')           # 97
    chr(97)            # 'a'
    ord('c') - ord('a')  # 2 (useful for index mapping)


# ============================================================
# 8. LIST COMPREHENSION POWER MOVES
# ============================================================

def comprehension_tricks():
    # --- Flatten 2D list ---
    matrix = [[1, 2], [3, 4], [5, 6]]
    flat = [x for row in matrix for x in row]  # [1,2,3,4,5,6]
    
    # --- Initialize 2D array (CORRECT way) ---
    rows, cols = 3, 4
    grid = [[0] * cols for _ in range(rows)]  # ✅
    # grid = [[0] * cols] * rows  # ❌ WRONG — shared references!
    
    # --- Filter and transform ---
    nums = [1, -2, 3, -4, 5]
    positives = [x for x in nums if x > 0]       # [1, 3, 5]
    squared = [x**2 for x in nums]                # [1, 4, 9, 16, 25]
    
    # --- Dict comprehension ---
    nums = [1, 2, 3]
    index_map = {v: i for i, v in enumerate(nums)}  # {1:0, 2:1, 3:2}
    
    # --- Set comprehension ---
    evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}


# ============================================================
# 9. USEFUL PATTERNS
# ============================================================

def useful_patterns():
    # --- Infinity ---
    min_val = float('inf')
    max_val = float('-inf')
    
    # --- Enumerate with index ---
    for i, val in enumerate([10, 20, 30]):
        pass  # i=0,val=10  i=1,val=20  i=2,val=30
    
    # --- Zip for parallel iteration ---
    a = [1, 2, 3]
    b = [4, 5, 6]
    for x, y in zip(a, b):
        pass  # (1,4), (2,5), (3,6)
    
    # --- Unpack ---
    a, b, *rest = [1, 2, 3, 4, 5]  # a=1, b=2, rest=[3,4,5]
    
    # --- Swap without temp ---
    a, b = b, a
    
    # --- Prefix sum with accumulate ---
    from itertools import accumulate
    nums = [1, 2, 3, 4, 5]
    prefix = list(accumulate(nums))           # [1, 3, 6, 10, 15]
    prefix = [0] + list(accumulate(nums))     # [0, 1, 3, 6, 10, 15] — with leading 0
    # Sum of nums[i:j] = prefix[j] - prefix[i]
    
    # --- @lru_cache for memoization (top-down DP) ---
    @lru_cache(maxsize=None)
    def fib(n):
        if n <= 1: return n
        return fib(n-1) + fib(n-2)
    
    # --- Divmod for quotient and remainder ---
    q, r = divmod(17, 5)  # q=3, r=2


# ============================================================
# 10. INTERVIEW-SPECIFIC SHORTCUTS
# ============================================================

def interview_shortcuts():
    # --- Check if power of 2 ---
    def is_power_of_2(n):
        return n > 0 and (n & (n - 1)) == 0
    
    # --- Get all subsets of a list ---
    def get_subsets(nums):
        result = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result
    
    # --- Matrix 4-directional neighbors ---
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    def get_neighbors(r, c, rows, cols):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc
    
    # --- Convert adjacency list to graph ---
    def build_graph(edges, directed=False):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            if not directed:
                graph[v].append(u)
        return graph
    
    # --- Trie node ---
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False


# ============================================================
# 11. COMMON GOTCHAS TO AVOID
# ============================================================

"""
GOTCHA 1: Mutable default arguments
  ❌ def f(arr=[]):        # Shared across calls!
  ✅ def f(arr=None): arr = arr or []

GOTCHA 2: Integer division
  ❌ -7 // 2 = -4          # Python floors toward negative infinity
  ✅ int(-7 / 2) = -3      # Truncates toward zero (like C++/Java)

GOTCHA 3: Modifying list while iterating
  ❌ for x in arr: arr.remove(x)
  ✅ arr = [x for x in arr if condition]

GOTCHA 4: Deep copy vs shallow copy
  ❌ b = a[:]              # Shallow copy — nested lists still shared
  ✅ import copy; b = copy.deepcopy(a)

GOTCHA 5: String concatenation in loop
  ❌ s = ""; for c in arr: s += c    # O(N²)
  ✅ s = ''.join(arr)                # O(N)

GOTCHA 6: Dictionary ordering
  ✅ Python 3.7+: dict preserves insertion order

GOTCHA 7: Max recursion depth
  Default is 1000. For deep recursion:
  import sys; sys.setrecursionlimit(10**6)
  Better: convert to iterative with explicit stack
"""
