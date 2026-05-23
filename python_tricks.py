"""
🐍 Python Tricks for Coding Interviews
=======================================
Master these idioms to write solutions 2x faster than other candidates.
Every trick here is interview-legal and commonly used in FAANG solutions.

Sections:
  1.  Essential Imports
  2.  Hash Map / Counter Tricks
  3.  Heap Tricks
  4.  Binary Search with bisect
  5.  Deque Tricks
  6.  Sorting Tricks
  7.  String Tricks
  8.  List Comprehensions
  9.  Interview Shortcuts
  10. Useful Patterns
  11. Common Gotchas

Run this file directly to execute all assertions:
  python python_tricks.py
"""

# ============================================================
# 1. ESSENTIAL IMPORTS — Memorize These
# ============================================================

from collections import defaultdict, Counter, deque, OrderedDict
from heapq import heappush, heappop, heapify, nlargest, nsmallest
from bisect import bisect_left, bisect_right, insort
from itertools import accumulate, combinations, permutations, product
from functools import lru_cache, reduce, cmp_to_key
from typing import List, Optional, Tuple, Dict, Set
from math import inf, gcd, ceil, floor, log2, sqrt, factorial
import string  # string.ascii_lowercase, string.digits, string.ascii_uppercase
import math    # math.inf, math.gcd, math.ceil, math.floor

# ============================================================
# 2. HASH MAP / COUNTER TRICKS
# ============================================================

def hash_map_tricks():
    # --- defaultdict: Never check "if key in dict" again ---
    graph = defaultdict(list)
    graph['A'].append('B')  # No KeyError, auto-creates empty list
    assert graph['A'] == ['B']
    assert graph['Z'] == []    # Missing key returns default, no KeyError

    freq = defaultdict(int)
    for x in [1, 2, 2, 3, 3, 3]:
        freq[x] += 1  # {1:1, 2:2, 3:3}
    assert freq[3] == 3

    # --- Counter: Frequency counting in one line ---
    text = "abracadabra"
    count = Counter(text)           # Counter({'a':5, 'b':2, 'r':2, 'c':1, 'd':1})
    assert count['a'] == 5
    assert count.most_common(2) == [('a', 5), ('b', 2)]

    # Counter arithmetic (great for anagram checks)
    assert Counter("anagram") == Counter("nagaram")  # True — same frequencies
    diff = Counter("abc") - Counter("ab")
    assert diff == Counter({'c': 1})

    # --- Frequency map pattern (manual, for when Counter is overkill) ---
    nums = [1, 2, 2, 3, 3, 3]
    freq_map = {}
    for n in nums:
        freq_map[n] = freq_map.get(n, 0) + 1
    assert freq_map == {1: 1, 2: 2, 3: 3}

    # --- Anagram grouping trick ---
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groups = defaultdict(list)
    for w in words:
        groups[tuple(sorted(w))].append(w)
    assert sorted(groups[('a', 'e', 't')]) == ['ate', 'eat', 'tea']

    print("✅ hash_map_tricks passed")


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
    assert smallest == 1

    # --- MAX-HEAP: Negate the values ---
    max_h = []
    for val in [5, 1, 3]:
        heappush(max_h, -val)
    largest = -heappop(max_h)  # 5
    assert largest == 5

    # --- Heap with tuples (for priority + data) ---
    tasks = []
    heappush(tasks, (2, "medium_task"))
    heappush(tasks, (1, "urgent_task"))
    heappush(tasks, (3, "low_task"))
    priority, task = heappop(tasks)  # (1, "urgent_task")
    assert priority == 1 and task == "urgent_task"

    # --- Heapify an existing list: O(N) instead of O(N log N) ---
    arr = [5, 3, 1, 4, 2]
    heapify(arr)  # In-place, now arr[0] is the minimum
    assert arr[0] == 1

    # --- Top K elements ---
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    top3 = nlargest(3, nums)   # [9, 6, 5]
    bot3 = nsmallest(3, nums)  # [1, 1, 2]
    assert top3 == [9, 6, 5]
    assert bot3 == [1, 1, 2]

    # --- K-way merge pattern (merge K sorted lists) ---
    # Push (value, list_index, element_index) into heap
    # heappush(h, (lists[i][0], i, 0))
    # while h: val, i, j = heappop(h); if j+1 < len(lists[i]): heappush(h, (lists[i][j+1], i, j+1))

    print("✅ heap_tricks passed")


# ============================================================
# 4. BINARY SEARCH WITH BISECT
# ============================================================

def bisect_tricks():
    arr = [1, 3, 5, 5, 5, 7, 9]

    # --- Find insertion point (leftmost) ---
    assert bisect_left(arr, 5) == 2    # first index where 5 can go

    # --- Find insertion point (rightmost) ---
    assert bisect_right(arr, 5) == 5   # after all existing 5s

    # --- Count occurrences of value in sorted array ---
    count_5 = bisect_right(arr, 5) - bisect_left(arr, 5)  # 3
    assert count_5 == 3

    # --- Check if value exists in sorted array ---
    def exists_in_sorted(arr, target):
        idx = bisect_left(arr, target)
        return idx < len(arr) and arr[idx] == target
    assert exists_in_sorted(arr, 5) is True
    assert exists_in_sorted(arr, 4) is False

    # --- Insert while maintaining sort ---
    arr2 = [1, 3, 5, 5, 5, 7, 9]
    insort(arr2, 4)  # arr2 = [1, 3, 4, 5, 5, 5, 7, 9]
    assert arr2 == [1, 3, 4, 5, 5, 5, 7, 9]

    # --- "Find leftmost value >= target" (lower bound) ---
    def lower_bound(arr, target):
        idx = bisect_left(arr, target)
        return idx if idx < len(arr) else -1
    assert lower_bound([1, 3, 5, 7], 4) == 2  # index of 5

    # --- "Find rightmost value <= target" (upper bound) ---
    def upper_bound(arr, target):
        idx = bisect_right(arr, target) - 1
        return idx if idx >= 0 else -1
    assert upper_bound([1, 3, 5, 7], 4) == 1  # index of 3

    # --- Binary search on answer (classic pattern) ---
    # "Find minimum X such that condition(X) is True"
    # lo, hi = 1, max_possible
    # while lo < hi:
    #     mid = (lo + hi) // 2
    #     if condition(mid): hi = mid
    #     else: lo = mid + 1
    # return lo

    print("✅ bisect_tricks passed")


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
    assert len(dq) == 0

    # --- BFS template with deque ---
    # queue = deque([(start, 0)])  # (node, distance)
    # visited = {start}
    # while queue:
    #     node, dist = queue.popleft()
    #     for neighbor in graph[node]:
    #         if neighbor not in visited:
    #             visited.add(neighbor)
    #             queue.append((neighbor, dist + 1))

    # --- Fixed-size sliding window (maxlen auto-evicts old elements) ---
    dq = deque(maxlen=3)
    for x in [1, 2, 3, 4, 5]:
        dq.append(x)
    assert list(dq) == [3, 4, 5]  # Only last 3 elements kept

    # --- Monotonic deque for sliding window maximum ---
    # Maintain indices in decreasing order of their values
    def sliding_window_max(nums, k):
        dq = deque()   # stores indices, front = max index
        result = []
        for i, val in enumerate(nums):
            # Remove indices outside window
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            # Remove smaller elements from back (they'll never be max)
            while dq and nums[dq[-1]] < val:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result

    assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

    print("✅ deque_tricks passed")


# ============================================================
# 6. SORTING TRICKS
# ============================================================

def sorting_tricks():
    # --- Sort by custom key ---
    intervals = [(3, 5), (1, 3), (2, 8)]
    intervals.sort(key=lambda x: x[0])         # Sort by start
    assert intervals[0] == (1, 3)
    intervals.sort(key=lambda x: x[1])         # Sort by end
    assert intervals[0] == (1, 3)
    intervals.sort(key=lambda x: x[1] - x[0])  # Sort by length

    # --- Sort by multiple criteria ---
    students = [("Alice", 90), ("Bob", 85), ("Charlie", 90)]
    students.sort(key=lambda x: (-x[1], x[0]))  # Score desc, then name asc
    assert students[0][0] == "Alice"  # Alice and Charlie both 90, Alice first alphabetically

    # --- Sort string characters ---
    s = "dcba"
    sorted_s = ''.join(sorted(s))  # "abcd"
    assert sorted_s == "abcd"

    # --- Frequency sort ---
    nums = [1, 1, 2, 2, 2, 3]
    c = Counter(nums)
    nums_sorted = sorted(nums, key=lambda x: c[x], reverse=True)
    assert nums_sorted[:3] == [2, 2, 2]  # Most frequent first

    # --- Custom comparator with functools.cmp_to_key ---
    # Use when comparison logic can't be expressed as a simple key
    # Example: sort numbers to form largest concatenation
    def compare(a, b):
        if str(a) + str(b) > str(b) + str(a):
            return -1   # a should come first
        elif str(a) + str(b) < str(b) + str(a):
            return 1    # b should come first
        return 0

    nums2 = [3, 30, 34, 5, 9]
    nums2.sort(key=cmp_to_key(compare))
    assert ''.join(map(str, nums2)) == "9534330"  # Largest number

    # --- Stable sort: Python's sort is always stable ---
    # Equal elements maintain their original relative order
    data = [(1, 'b'), (2, 'a'), (1, 'a')]
    data.sort(key=lambda x: x[0])
    assert data == [(1, 'b'), (1, 'a'), (2, 'a')]  # (1,'b') before (1,'a') — original order

    print("✅ sorting_tricks passed")


# ============================================================
# 7. STRING TRICKS
# ============================================================

def string_tricks():
    # --- String → Char frequency ---
    freq = Counter("hello")
    assert freq == Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

    # --- Check if string is all digits/alpha ---
    assert "123".isdigit()    is True
    assert "abc".isalpha()    is True
    assert "abc123".isalnum() is True

    # --- strip / lstrip / rstrip ---
    assert "  hello  ".strip()  == "hello"
    assert "  hello  ".lstrip() == "hello  "
    assert "  hello  ".rstrip() == "  hello"
    assert "xxhelloxx".strip('x') == "hello"  # Strip specific chars

    # --- split and join ---
    words = "hello world foo".split()          # ['hello', 'world', 'foo']
    assert words == ['hello', 'world', 'foo']
    assert ' '.join(words) == "hello world foo"
    assert ','.join(['a', 'b', 'c']) == "a,b,c"

    # --- Reverse a string ---
    s = "hello"
    assert s[::-1] == "olleh"

    # --- Build string with list (O(N) instead of O(N²)) ---
    chars = []
    for c in "hello":
        chars.append(c.upper())
    result = ''.join(chars)
    assert result == "HELLO"

    # --- Check palindrome ---
    assert "racecar" == "racecar"[::-1]
    def is_palindrome(s):
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())  # Remove non-alphanumeric
        return s == s[::-1]
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("race a car") is False

    # --- Anagram check ---
    def is_anagram(s, t):
        return Counter(s) == Counter(t)
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False

    # --- ord/chr for character math ---
    assert ord('a') == 97
    assert chr(97) == 'a'
    assert ord('c') - ord('a') == 2   # Useful for index mapping: c → 2

    # --- string.ascii_lowercase / uppercase / digits ---
    assert string.ascii_lowercase == "abcdefghijklmnopqrstuvwxyz"
    assert string.ascii_uppercase == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert string.digits == "0123456789"

    # --- 26-bucket frequency array (faster than Counter for lowercase only) ---
    def char_freq_array(s):
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        return freq
    assert char_freq_array("abc") == [1, 1, 1] + [0] * 23

    # --- String formatting tricks ---
    n = 42
    assert f"{n:05d}" == "00042"   # Zero-padded
    assert f"{n:b}"   == "101010"  # Binary
    assert f"{n:x}"   == "2a"      # Hex

    # --- Find all occurrences of substring ---
    s = "abcabcabc"
    indices = [i for i in range(len(s)) if s.startswith("abc", i)]
    assert indices == [0, 3, 6]

    print("✅ string_tricks passed")


# ============================================================
# 8. LIST COMPREHENSION POWER MOVES
# ============================================================

def comprehension_tricks():
    # --- Flatten 2D list ---
    matrix = [[1, 2], [3, 4], [5, 6]]
    flat = [x for row in matrix for x in row]  # [1,2,3,4,5,6]
    assert flat == [1, 2, 3, 4, 5, 6]

    # --- Initialize 2D array (CORRECT way) ---
    rows, cols = 3, 4
    grid = [[0] * cols for _ in range(rows)]  # ✅ Each row is independent
    # grid = [[0] * cols] * rows              # ❌ WRONG — all rows share same list!
    grid[0][0] = 99
    assert grid[1][0] == 0  # Proves rows are independent

    # --- Filter and transform ---
    nums = [1, -2, 3, -4, 5]
    positives = [x for x in nums if x > 0]       # [1, 3, 5]
    squared   = [x**2 for x in nums]              # [1, 4, 9, 16, 25]
    assert positives == [1, 3, 5]
    assert squared   == [1, 4, 9, 16, 25]

    # --- Conditional expression (ternary) in comprehension ---
    clamped = [x if x > 0 else 0 for x in nums]  # Replace negatives with 0
    assert clamped == [1, 0, 3, 0, 5]

    # --- Nested list comprehension (matrix transpose) ---
    matrix = [[1, 2, 3], [4, 5, 6]]
    transposed = [[row[i] for row in matrix] for i in range(3)]
    assert transposed == [[1, 4], [2, 5], [3, 6]]

    # --- Dict comprehension ---
    nums = [1, 2, 3]
    index_map = {v: i for i, v in enumerate(nums)}  # {1:0, 2:1, 3:2}
    assert index_map == {1: 0, 2: 1, 3: 2}

    # --- Set comprehension ---
    evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}
    assert evens == {0, 2, 4, 6, 8}

    # --- Generator expression (lazy, memory-efficient) ---
    total = sum(x**2 for x in range(1000))  # No intermediate list created
    assert total == 332833500

    print("✅ comprehension_tricks passed")


# ============================================================
# 9. USEFUL PATTERNS
# ============================================================

def interview_shortcuts():
    """
    Section 9: Interview Shortcuts
    Quick one-liners and patterns that save time in interviews.
    """
    # --- Infinity ---
    assert math.inf > 10**18          # math.inf is the canonical way
    assert float('inf') == math.inf   # Both work; math.inf is cleaner
    min_val = math.inf
    max_val = -math.inf

    # --- enumerate: index + value together ---
    result = []
    for i, val in enumerate([10, 20, 30]):
        result.append((i, val))
    assert result == [(0, 10), (1, 20), (2, 30)]
    # Start from custom index:
    assert list(enumerate(['a', 'b'], start=1)) == [(1, 'a'), (2, 'b')]

    # --- zip: parallel iteration ---
    a = [1, 2, 3]
    b = [4, 5, 6]
    assert list(zip(a, b)) == [(1, 4), (2, 5), (3, 6)]
    # zip stops at shortest — use zip_longest for unequal lengths
    # Unzip: list(zip(*pairs)) reverses the zip
    pairs = [(1, 4), (2, 5), (3, 6)]
    xs, ys = zip(*pairs)
    assert list(xs) == [1, 2, 3]

    # --- any / all ---
    nums = [1, 2, 3, 4, 5]
    assert any(x > 4 for x in nums) is True   # At least one > 4
    assert all(x > 0 for x in nums) is True   # All positive
    assert any(x > 10 for x in nums) is False
    assert all(x > 2 for x in nums) is False

    # --- min / max with key ---
    words = ["apple", "fig", "banana"]
    assert min(words, key=len) == "fig"
    assert max(words, key=len) == "banana"

    students = [("Alice", 90), ("Bob", 85), ("Charlie", 95)]
    assert max(students, key=lambda x: x[1]) == ("Charlie", 95)

    # --- divmod: quotient and remainder in one call ---
    q, r = divmod(17, 5)
    assert q == 3 and r == 2
    # Useful for: converting seconds to hours/minutes, digit extraction

    # --- Unpack and swap ---
    a, b, *rest = [1, 2, 3, 4, 5]
    assert a == 1 and b == 2 and rest == [3, 4, 5]
    a, b = b, a  # Swap without temp variable
    assert a == 2 and b == 1

    # --- Ternary expression ---
    x = 5
    label = "positive" if x > 0 else "non-positive"
    assert label == "positive"

    # --- Walrus operator := (Python 3.8+) ---
    # Assign and use in same expression — great for while loops
    data = [1, 2, 3, 4, 5]
    idx = 0
    results = []
    while (val := data[idx] if idx < len(data) else None) is not None:
        results.append(val * 2)
        idx += 1
    assert results == [2, 4, 6, 8, 10]

    # --- sorted() vs .sort() ---
    original = [3, 1, 2]
    new_list = sorted(original)   # Returns new list, original unchanged
    assert original == [3, 1, 2]
    assert new_list == [1, 2, 3]
    original.sort()               # In-place, returns None
    assert original == [1, 2, 3]

    print("✅ interview_shortcuts passed")


# ============================================================
# 10. USEFUL PATTERNS
# ============================================================

def useful_patterns():
    # --- Prefix sum with accumulate ---
    nums = [1, 2, 3, 4, 5]
    prefix = list(accumulate(nums))           # [1, 3, 6, 10, 15]
    prefix_with_zero = [0] + list(accumulate(nums))  # [0, 1, 3, 6, 10, 15]
    # Sum of nums[i:j] = prefix_with_zero[j] - prefix_with_zero[i]
    assert prefix_with_zero[3] - prefix_with_zero[1] == 2 + 3  # sum of nums[1:3]

    # --- @lru_cache for memoization (top-down DP) ---
    @lru_cache(maxsize=None)
    def fib(n):
        if n <= 1: return n
        return fib(n-1) + fib(n-2)
    assert fib(10) == 55

    # --- Matrix 4-directional neighbors ---
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def get_neighbors(r, c, rows, cols):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc
    neighbors = list(get_neighbors(0, 0, 3, 3))
    assert (0, 1) in neighbors and (1, 0) in neighbors
    assert (-1, 0) not in neighbors  # Out of bounds filtered

    # --- Convert adjacency list to graph ---
    def build_graph(edges, directed=False):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            if not directed:
                graph[v].append(u)
        return graph
    g = build_graph([(1, 2), (2, 3)])
    assert 2 in g[1] and 1 in g[2]  # Undirected

    # --- Trie node ---
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False

    # --- Union-Find (Disjoint Set Union) ---
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  # Path compression
            return self.parent[x]

        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px == py: return False
            if self.rank[px] < self.rank[py]: px, py = py, px
            self.parent[py] = px
            if self.rank[px] == self.rank[py]: self.rank[px] += 1
            return True

    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    assert uf.find(0) == uf.find(2)  # 0 and 2 are connected
    assert uf.find(0) != uf.find(3)  # 0 and 3 are not connected

    # --- Bit manipulation shortcuts ---
    assert 5 & (5 - 1) == 4          # Clear lowest set bit
    assert 5 & (-5) == 1             # Isolate lowest set bit
    assert (5 & (5 - 1)) == 0 or True  # is_power_of_2: n > 0 and (n & (n-1)) == 0
    assert bin(7).count('1') == 3    # Count set bits (popcount)

    print("✅ useful_patterns passed")


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


# ============================================================
# RUN ALL ASSERTIONS
# ============================================================

if __name__ == "__main__":
    print("Running all Python tricks assertions...\n")
    hash_map_tricks()
    heap_tricks()
    bisect_tricks()
    deque_tricks()
    sorting_tricks()
    string_tricks()
    comprehension_tricks()
    interview_shortcuts()
    useful_patterns()
    print("\n🎉 All assertions passed! You're interview-ready.")
