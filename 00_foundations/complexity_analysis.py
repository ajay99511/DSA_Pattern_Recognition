"""
📊 Complexity Analysis — The Foundation of Everything
=====================================================
If you can't analyze complexity, you can't choose algorithms.
This is the FIRST thing interviewers evaluate.

Master this file and you'll instantly know:
1. Whether your solution will TLE
2. Which algorithm class to use based on constraints
3. How to communicate complexity clearly
"""


# ============================================================
# PART 1: BIG-O INTUITION
# ============================================================

"""
Big-O tells you HOW FAST your runtime grows as input grows.

Mental model: "If I 10x the input, how much slower does it get?"

O(1)       → Same speed           → Hash map lookup
O(log N)   → Barely slower        → Binary search (10x input = ~3 more steps)
O(N)       → 10x slower           → Single loop
O(N log N) → ~13x slower          → Sorting
O(N²)      → 100x slower          → Nested loops
O(2^N)     → Impossibly slower    → Subsets/backtracking
O(N!)      → Universe dies first  → Permutations

RULE OF THUMB: ~10^8 operations per second in Python.
"""


# ============================================================
# PART 2: ANALYZING LOOPS
# ============================================================

def example_O1():
    """O(1) — Constant time. Doesn't depend on input size."""
    arr = [1, 2, 3, 4, 5]
    return arr[0] + arr[-1]  # Always 2 operations


def example_ON(arr):
    """O(N) — Linear. One pass through the data."""
    total = 0
    for x in arr:           # N iterations
        total += x          # O(1) per iteration
    return total            # Total: O(N)


def example_ON2(arr):
    """O(N²) — Quadratic. Nested loop over same data."""
    count = 0
    for i in range(len(arr)):       # N iterations
        for j in range(len(arr)):   # N iterations each
            if arr[i] + arr[j] == 0:
                count += 1
    return count                     # Total: O(N × N) = O(N²)


def example_ON_log_N(arr):
    """O(N log N) — Linearithmic. Sorting, then one pass."""
    arr.sort()              # O(N log N)
    for x in arr:           # O(N)
        pass
    # Total: O(N log N) + O(N) = O(N log N)  ← dominant term wins


def example_O_log_N(arr, target):
    """O(log N) — Logarithmic. Halving the search space each step."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:             # log₂(N) iterations
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# ============================================================
# PART 3: COMMON PATTERNS AND THEIR COMPLEXITIES
# ============================================================

"""
PATTERN → TIME COMPLEXITY → EXAMPLE

Single loop over N           → O(N)        → Two pointers, sliding window
Nested loops (same array)    → O(N²)       → Brute force pair finding
Sort + single loop           → O(N log N)  → Sort + two pointers
Binary search                → O(log N)    → Finding target in sorted array
Hash map + single loop       → O(N)        → Two sum with hash map
BFS/DFS on graph             → O(V + E)    → Graph traversal
Heap with N insertions       → O(N log N)  → Building priority queue
DP with N states             → O(N)        → Fibonacci, house robber
DP with N×M states           → O(N×M)      → Edit distance, grid DP
Backtracking (subsets)       → O(2^N)      → Subset generation
Backtracking (permutations)  → O(N!)       → Permutation generation
"""


# ============================================================
# PART 4: SPACE COMPLEXITY
# ============================================================

"""
Space complexity = EXTRA memory used (not counting input).

O(1) space:
  - A few variables, constant-size arrays
  - Two pointers, in-place sorting
  - Example: Reversing an array in-place

O(N) space:
  - Hash map, hash set, new array of size N
  - Recursion call stack of depth N
  - Example: Storing frequency counts

O(N×M) space:
  - 2D DP table, adjacency matrix
  - Example: Edit distance DP

COMMON TRAP: Recursion uses O(depth) stack space!
  - DFS on balanced tree: O(log N)
  - DFS on skewed tree: O(N)
  - DFS on graph: O(V)
"""


def space_O1_example(arr):
    """O(1) extra space — in-place two-pointer reversal."""
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    # Only used 2 extra variables: left, right


def space_ON_example(arr):
    """O(N) extra space — hash set for lookup."""
    seen = set()             # Grows up to N elements
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False


# ============================================================
# PART 5: AMORTIZED ANALYSIS
# ============================================================

"""
Amortized = "average cost per operation over many operations"

Key example: Python list.append()
  - Usually O(1)
  - Occasionally O(N) when the list needs to resize
  - BUT averaged over N appends: O(1) per append
  - Therefore: AMORTIZED O(1)

Where it matters:
  - list.append()         → Amortized O(1) ✅
  - list.insert(0, x)     → Always O(N) ❌  (use deque.appendleft)
  - dict[key] = val       → Amortized O(1) ✅
  - Union-Find with path compression → Amortized O(α(N)) ≈ O(1)
"""


# ============================================================
# PART 6: HOW TO COMMUNICATE COMPLEXITY IN INTERVIEWS
# ============================================================

"""
TEMPLATE for communicating complexity:

"The time complexity is O(N log N) because:
 - We sort the array first, which takes O(N log N)
 - Then we do a single pass with two pointers, which is O(N)
 - The dominant term is O(N log N)

The space complexity is O(1) because:
 - We sort in-place
 - We only use two pointer variables"

ADVANCED: When asked "can you do better?"
 - If you're at O(N log N) with sorting, ask: "Can I avoid sorting?"
   → Usually means hash map for O(N)
 - If you're at O(N) time + O(N) space, ask: "Can I reduce space?"
   → Usually means two pointers or in-place modification for O(1) space
 - If you're at O(N²), ask: "What's repeated work I can cache?"
   → Usually means hash map, prefix sum, or DP
"""


# ============================================================
# EXERCISES: Practice Analyzing These
# ============================================================

def exercise_1(arr):
    """What's the time complexity? Analyze step by step."""
    arr.sort()                           # ?
    result = []                          # ?
    for i in range(len(arr)):            # ?
        if i == 0 or arr[i] != arr[i-1]: # ?
            result.append(arr[i])        # ?
    return result
    # ANSWER: O(N log N) for sort + O(N) for loop = O(N log N)
    # Space: O(N) for result array (O(1) if we don't count output)


def exercise_2(s):
    """What's the time complexity?"""
    from collections import Counter
    count = Counter(s)                   # ?
    for char, freq in count.items():     # ?
        if freq == 1:                    # ?
            return char                  # ?
    return ''
    # ANSWER: O(N) to build counter + O(26) to iterate = O(N)
    # Space: O(26) = O(1) for the counter (bounded alphabet)


def exercise_3(matrix):
    """What's the time complexity?"""
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):               # ?
        for j in range(cols):           # ?
            for k in range(rows):       # ?
                matrix[i][j] += matrix[k][j]  # ?
    # ANSWER: O(rows × cols × rows) = O(N² × M) or O(N²M)
    # Space: O(1)


if __name__ == "__main__":
    print("✅ Complexity Analysis module loaded.")
    print("Study the patterns above, then test yourself with the exercises.")
    print("Key insight: Constraints tell you the algorithm class!")
