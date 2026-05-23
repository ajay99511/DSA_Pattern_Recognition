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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6A. THE STANDARD COMPLEXITY EXPLANATION TEMPLATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Use this structure EVERY time you explain complexity:

  "The time complexity is O(___) because [reason].
   The space complexity is O(___) because [reason]."

FULL EXAMPLE (Sort + Two Pointers):
  "The time complexity is O(N log N) because:
   - We sort the array first, which takes O(N log N)
   - Then we do a single pass with two pointers, which is O(N)
   - The dominant term is O(N log N), so overall O(N log N)

   The space complexity is O(1) because:
   - We sort in-place (no extra array)
   - We only use two pointer variables — constant extra space"

FULL EXAMPLE (Hash Map):
  "The time complexity is O(N) because:
   - We make a single pass through the array
   - Each hash map lookup and insert is O(1) amortized
   - So N iterations × O(1) each = O(N) total

   The space complexity is O(N) because:
   - In the worst case, we store all N elements in the hash map"

FULL EXAMPLE (BFS/DFS on Graph):
  "The time complexity is O(V + E) because:
   - We visit each vertex exactly once: O(V)
   - We process each edge exactly once: O(E)
   - Total work is proportional to vertices plus edges

   The space complexity is O(V) because:
   - The queue (BFS) or call stack (DFS) holds at most V nodes
   - The visited set also holds at most V nodes"

FULL EXAMPLE (DP):
  "The time complexity is O(N × M) because:
   - We fill an N × M DP table
   - Each cell takes O(1) to compute
   - Total: N × M cells × O(1) = O(N × M)

   The space complexity is O(N × M) for the DP table,
   or O(min(N, M)) if we optimize to use only two rows."

FULL EXAMPLE (Backtracking / Subsets):
  "The time complexity is O(2^N × N) because:
   - There are 2^N possible subsets
   - Each subset takes O(N) to copy into the result
   - Total: O(2^N × N)

   The space complexity is O(N) for the recursion call stack depth,
   not counting the output."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6B. PRE-CODING COMPLEXITY ANNOUNCEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before writing code, state your expected complexity:

  "Before I code this up — I expect this approach to be
   O(N log N) time and O(1) space. Let me know if you'd
   like me to aim for something better before I start."

This signals:
  ✅ You know the complexity before coding (not after)
  ✅ You're giving the interviewer a chance to redirect
  ✅ You're thinking about tradeoffs, not just correctness

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6C. RESPONDING TO "CAN YOU DO BETTER?"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Don't panic. Use this decision tree:

  Currently O(N²)?
    → "The repeated work is [X]. I can cache it with a hash map → O(N)"
    → "I can sort first and use two pointers → O(N log N)"

  Currently O(N log N) with sorting?
    → "If I can avoid sorting, I can use a hash map → O(N)"
    → "The sort is the bottleneck. Without it, the rest is O(N)."

  Currently O(N) time + O(N) space?
    → "I can trade space for time using two pointers → O(1) space"
    → "The hash map is for O(1) lookup. Without it, I'd need O(N log N) time."

  Currently O(2^N)?
    → "This is inherently exponential — we must enumerate all subsets."
    → "With memoization, I can reduce overlapping subproblems → O(N × states)"

  Script for "can you do better?":
    "Let me think about what's driving the current complexity...
     [pause 5 seconds]
     The bottleneck is [X]. If I [change Y], I could get to [better complexity].
     The tradeoff is [Z]. Want me to implement that instead?"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6D. COMMON INTERVIEWER FOLLOW-UP QUESTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q: "What's the time complexity of your solution?"
A: Use Template 6A above. Always break it down step by step.

Q: "What about space complexity?"
A: "The space complexity is O(___). This accounts for [extra data structures].
    I'm not counting the input itself, only the extra memory I allocate."

Q: "Is this optimal?"
A: "For comparison-based sorting, O(N log N) is the theoretical lower bound.
    For this problem, O(N) is achievable with a hash map because [reason]."
    — OR —
    "I believe O(N) is optimal here because we must read every element at least once."

Q: "What if N is very large — say 10^9?"
A: "At 10^9, even O(N) would be ~10 seconds in Python. I'd need O(log N) or O(1).
    That suggests binary search or a mathematical formula."

Q: "What's the worst case vs average case?"
A: "The worst case is O(N²) — for example, a sorted array with a bad pivot in quicksort.
    The average case is O(N log N) with random pivot selection.
    For interviews, I always state worst case unless asked otherwise."

Q: "Does your solution handle the constraints?"
A: "The constraint is N ≤ 10^5. My solution is O(N log N) ≈ 10^5 × 17 ≈ 1.7 × 10^6
    operations. Well within the ~10^8 ops/second limit. ✅"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6E. CONSTRAINT → COMPLEXITY CHEAT SHEET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Use this to instantly know what complexity is REQUIRED:

  N ≤ 10        → O(N!) or O(2^N) is fine   → Brute force / backtracking
  N ≤ 20        → O(2^N) is fine             → Bitmask DP, subsets
  N ≤ 100       → O(N³) is fine              → Floyd-Warshall, 3-nested loops
  N ≤ 1,000     → O(N²) is fine              → Brute force pairs, O(N²) DP
  N ≤ 10^5      → O(N log N) required        → Sort + linear, heap, binary search
  N ≤ 10^6      → O(N) required              → Single pass, hash map
  N ≤ 10^9      → O(log N) or O(1) required  → Binary search, math formula

  Script: "The constraint is N ≤ [X], which tells me I need at most O([Y]).
           My approach is O([Z]), which fits within that budget."
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
