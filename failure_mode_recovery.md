# 🚨 Failure-Mode Recovery Protocol

> **Purpose**: What to do when you're STUCK in an interview. The plan teaches you what to do when you recognize the pattern. This teaches what to do when you DON'T — or when you picked the wrong one.

---

## The 3 Failure Modes

### Mode 1: "I Have No Idea" (Blank — 0 Minutes In)

**You read the problem and nothing clicks. No pattern comes to mind.**

```
TIMER: You have 3 MINUTES max before you must act.

ACTION SEQUENCE:

1. BRUTE FORCE FIRST
   → Write the O(n²) or O(2^n) solution in your head (don't code it)
   → Ask: "What's EXPENSIVE about this? What am I recomputing?"
   → The answer often reveals the pattern:
     • "I'm scanning the whole array each time" → Hash Map / Two Pointers
     • "I'm recomputing the same subproblems" → DP (add memoization)
     • "I'm checking all pairs" → Sort first, then Two Pointers / Binary Search

2. CONSTRAINT CHECK
   Look at N. The constraints TELL you the algorithm:
   ┌──────────────┬─────────────────┬──────────────────────────────────┐
   │ N ≤ 10-12    │ O(N!) or O(2^N) │ Backtracking, Bitmask DP         │
   │ N ≤ 20       │ O(2^N × N)      │ Bitmask DP                       │
   │ N ≤ 300      │ O(N³)           │ Floyd-Warshall, 2D DP            │
   │ N ≤ 1,000    │ O(N²)           │ 2D DP, nested loops              │
   │ N ≤ 100,000  │ O(N log N)      │ Sorting, Binary Search, Heap     │
   │ N ≤ 1,000,000│ O(N)            │ Hash Map, Two Pointers, Sliding  │
   │ N ≤ 10^9     │ O(log N)        │ Binary Search, Math              │
   └──────────────┴─────────────────┴──────────────────────────────────┘

3. DATA STRUCTURE HINT
   Ask: "What data structure makes the brute force FASTER?"
   • Need fast lookup?      → Hash Map / Hash Set
   • Need ordering?         → Heap or Sorted Container
   • Need range queries?    → Segment Tree / Prefix Sum
   • Need "next greater"?   → Monotonic Stack
   • Need to track groups?  → Union-Find

4. STILL STUCK? SIMPLIFY.
   → Solve for N=3 or N=4 by hand
   → The manual process often reveals the algorithm
```

**What to SAY out loud (critical for interview scoring):**

> "Let me start by thinking about the brute force approach — that would be O(n²) by checking every pair. But I notice the constraint is N=10^5, so I need something O(n log n) or better. Let me think about what data structure could eliminate the inner loop..."

---

### Mode 2: "I Picked a Pattern but I'm Stuck Implementing" (5-10 Minutes In)

**You identified the right (or wrong) pattern but can't get the code to work.**

```
TIMER: If you haven't made progress in 5 MINUTES on implementation, STOP.

SAY THIS:
"I'm going to step back and re-examine my approach."

DIAGNOSTIC CHECKLIST:

□ STATE DEFINITION (especially for DP)
  → "What exactly does dp[i] represent?"
  → Write it as a one-line comment BEFORE coding
  → If you can't define it clearly, your DP formulation is wrong

□ TRANSITION/RECURRENCE
  → "How do I get dp[i] from previous states?"
  → Trace through your recurrence with a small example (N=3)
  → Check: are you handling the base case?

□ DATA STRUCTURE MISMATCH
  → Are you using the right structure for the operations you need?
  → Example: Using a list when you need O(1) lookup → switch to set/dict

□ OFF-BY-ONE ERRORS
  → Classic: wrong loop bounds, wrong index in DP
  → Trace your code with the smallest non-trivial input

□ SIMPLIFY FIRST
  → Solve a SMALLER version of the problem first (N=3, N=4)
  → Get that working, THEN generalize
```

**What to SAY out loud:**

> "Let me verify my approach with this small example... [traces through]. I see the issue — my state transition isn't accounting for [X]. Let me adjust..."

---

### Mode 3: "My Solution Works but Is Too Slow" (TLE — 15+ Minutes In)

**Your solution is correct but exceeds the time limit. You need to optimize.**

```
OPTIMIZATION CHECKLIST (in order of likelihood):

1. CAN I PRECOMPUTE?
   → Prefix sum / Prefix product / Preprocessing step
   → Example: Instead of summing subarrays each time, precompute prefix sums

2. CAN I BINARY SEARCH INSTEAD OF LINEAR SCAN?
   → If you're doing a linear search inside a loop, check if the search
     space is monotonic → Binary Search drops O(N²) → O(N log N)

3. CAN I USE A MONOTONIC STACK/DEQUE?
   → If you're rescanning previous elements for "next greater" / "sliding max"
   → Monotonic deque: O(N²) → O(N)

4. AM I RECOMPUTING OVERLAPPING SUBPROBLEMS?
   → Add memoization: @lru_cache or dict
   → Recursion + memo = top-down DP

5. CAN I USE A HEAP INSTEAD OF SORTING REPEATEDLY?
   → If you sort after every insertion → Use a heap: O(N² log N) → O(N log N)

6. CAN I USE UNION-FIND INSTEAD OF REPEATED DFS?
   → If checking connectivity multiple times → Union-Find: O(α(N)) per query

7. AM I USING THE RIGHT ALGORITHM CLASS?
   → BFS vs DFS (BFS is often faster for shortest path)
   → Dijkstra vs Bellman-Ford (Dijkstra if no negative weights)
   → Bottom-up DP vs recursion (bottom-up avoids stack overhead)
```

**What to SAY out loud:**

> "My current approach is O(n²). The bottleneck is [this inner loop]. I think I can optimize by [precomputing / using a hash map / binary search] which would bring it down to O(n log n)."

---

## The Graceful Pivot Protocol

When you realize your initial approach is WRONG, don't panic. Follow this:

```
STEP 1: ACKNOWLEDGE (2 seconds)
  → "I realize this approach has a problem — [state the issue clearly]"

STEP 2: SALVAGE WHAT YOU CAN (10 seconds)  
  → "However, the [data structure / preprocessing] I set up is still useful"
  → Don't throw everything away if the setup is reusable

STEP 3: PIVOT (20 seconds)
  → "I think a better approach would be [new pattern] because [reason]"
  → Explain WHY the new approach avoids the pitfall of the old one

STEP 4: RESTART CLEANLY
  → Don't try to patch broken code — start the algorithm fresh
  → Keep helper functions / data structures that are still valid
```

**Exact phrase to use:**

> "I initially thought this was a [X] problem, but I'm noticing [observation] which suggests [Y] would be more efficient. Let me restructure my approach."

**Why this works:**
- Shows **metacognition** — you can evaluate your own thinking
- Shows **adaptability** — you can recover under pressure  
- This is an **L5+ signal** — junior engineers get stuck; senior engineers pivot

---

## Common Wrong-Pattern Traps

| Problem Type | Common Wrong Guess | Actually Is |
|-------------|-------------------|-------------|
| "Find pair with sum X" (unsorted) | Two Pointers | Hash Map (O(n) vs O(n log n)) |
| "Minimum window substring" | Two Pointers | Sliding Window + Hash Map |
| "Jump Game II" | DP | Greedy (BFS-like) |
| "Word Break" | Backtracking | DP with memoization |
| "Longest Palindromic Substring" | Two Pointers | Expand Around Center or DP |
| "Course Schedule" | DFS only | Topological Sort (Kahn's) |
| "Meeting Rooms II" | Sorting only | Sorting + Min Heap (or Sweep Line) |

---

## Daily Failure Drill (5 minutes/day)

Pick ONE problem you've never seen. Set a **3-minute timer**.

- If you identify the pattern → ✅ Move on
- If you DON'T → Use the Mode 1 protocol. Was the protocol effective?
- Track your success rate weekly. Target: >80% by week 8, >95% by week 20.
