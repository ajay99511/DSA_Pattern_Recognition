# 🧠 DSA Mastery Plan — FAANG-Level Problem Solving

> **Goal**: Build pattern-recognition instincts so strong that you can read *any* coding problem and identify the optimal approach within 60 seconds — even if you've just woken up.

---

## Core Philosophy

> [!IMPORTANT]
> **You are NOT memorizing solutions. You are building a pattern-matching neural network in your brain.**
> 
> There are ~2,500+ LeetCode problems, but they all decompose into **~15 core patterns**. Master the patterns, and every new problem becomes a *remix* of something you already know.

### The Three Pillars

| Pillar | What It Means | How We Achieve It |
|--------|--------------|-------------------|
| **Pattern Recognition** | See a problem → instantly know the technique | Decision-tree framework + signal-word training |
| **Template Fluency** | Know the skeleton code for each pattern by heart | Python templates you can write blindfolded |
| **Adaptive Problem Solving** | Handle novel twists and combinations | Deliberate practice on hybrid/hard problems |

---

## Proposed Structure — What We'll Build in Your Workspace

```
c:\Personal\Ajay_Work_Docs\Grad_Project\DSA\
├── 00_foundations/
│   ├── complexity_analysis.py        # Big-O cheatsheet + examples
│   ├── recursion_mastery.py          # Recursion mental model + templates
│   └── bit_manipulation.py           # Bit tricks compendium
├── 01_arrays_and_hashing/
│   ├── README.md                     # Pattern guide + recognition signals
│   ├── templates.py                  # Core templates (prefix sum, frequency map, etc.)
│   └── problems/                     # Solved problems with annotations
├── 02_two_pointers/
│   ├── README.md
│   ├── templates.py
│   └── problems/
├── 03_sliding_window/
│   ├── README.md
│   ├── templates.py
│   └── problems/
├── 04_binary_search/
│   ├── README.md
│   ├── templates.py
│   └── problems/
├── 05_stacks_and_queues/
│   ├── README.md                     # Includes Monotonic Stack/Queue
│   ├── templates.py
│   └── problems/
├── 06_linked_lists/
│   ├── README.md
│   ├── templates.py
│   └── problems/
├── 07_trees/
│   ├── README.md                     # BST, traversals, path problems
│   ├── templates.py
│   └── problems/
├── 08_tries/
│   ├── README.md
│   ├── templates.py
│   └── problems/
├── 09_heaps_and_priority_queues/
│   ├── README.md
│   ├── templates.py
│   └── problems/
├── 10_graphs/
│   ├── README.md                     # BFS, DFS, Dijkstra, Union-Find, Topo Sort
│   ├── templates.py
│   └── problems/
├── 11_backtracking/
│   ├── README.md
│   ├── templates.py
│   └── problems/
├── 12_dynamic_programming/
│   ├── README.md                     # 1D, 2D, knapsack, LCS, LIS, state machines
│   ├── templates.py
│   └── problems/
├── 13_greedy/
│   ├── README.md
│   ├── templates.py
│   └── problems/
├── 14_intervals/
│   ├── README.md
│   ├── templates.py
│   └── problems/
├── 15_math_and_geometry/
│   ├── README.md
│   ├── templates.py
│   └── problems/
├── pattern_decision_tree.md          # The "Which pattern?" flowchart
├── python_tricks.py                  # Python-specific idioms for interviews
├── complexity_cheatsheet.md          # One-page Big-O reference
└── spaced_repetition_tracker.md      # Review schedule tracker
```

---

## The 6 Phases of Mastery

### Phase 1: Foundations (Week 1-2)
> Build the mental infrastructure everything else depends on.

| Topic | Key Concepts | Why It Matters |
|-------|-------------|----------------|
| **Complexity Analysis** | Big-O notation, amortized analysis, space vs time tradeoffs | You MUST be able to analyze any solution's complexity instantly |
| **Recursion** | Base case identification, recursive leap of faith, call stack visualization | Foundation for Trees, Graphs, Backtracking, DP |
| **Bit Manipulation** | AND/OR/XOR tricks, checking/setting bits, power-of-2 checks | Appears in ~5-10% of interviews, easy points when you know it |
| **Python Mastery** | `collections`, `heapq`, `bisect`, `itertools`, `defaultdict`, `Counter`, sorting key functions, list comprehensions | Write solutions 2x faster than other candidates |

**Deliverables**: `00_foundations/` folder with annotated templates and exercises.

---

### Phase 2: Linear Patterns (Week 3-5)
> Master the patterns that solve ~40% of all interview problems.

| Module | Pattern | Recognition Signals |
|--------|---------|-------------------|
| `01_arrays_and_hashing` | Hash maps, frequency counting, prefix sums | "Find pair/group", "count occurrences", "subarray sum equals K" |
| `02_two_pointers` | Opposite-direction, same-direction, partitioning | "Sorted array", "pair with sum", "remove duplicates", "container with water" |
| `03_sliding_window` | Fixed window, variable window, with hash map | "Contiguous subarray/substring", "maximum/minimum of length K", "at most K distinct" |
| `04_binary_search` | Classic, on answer, on rotated array | "Sorted", "minimum/maximum that satisfies", "search space is monotonic" |
| `05_stacks_and_queues` | Monotonic stack, expression evaluation, BFS queue | "Next greater element", "valid parentheses", "daily temperatures" |
| `06_linked_lists` | Fast/slow pointers, dummy head, reversal | "Cycle detection", "middle element", "merge sorted lists", "reverse in groups" |

**Deliverables**: README + templates + 8-12 solved problems per module.

---

### Phase 3: Hierarchical Patterns (Week 6-8)
> Trees and Graphs — the backbone of ~30% of FAANG questions.

| Module | Pattern | Recognition Signals |
|--------|---------|-------------------|
| `07_trees` | DFS (pre/in/post), BFS (level-order), BST properties, path problems | "Binary tree", "lowest common ancestor", "validate BST", "max depth" |
| `08_tries` | Prefix matching, autocomplete, word search | "Prefix", "dictionary of words", "starts with", "word break" |
| `09_heaps` | Top-K, merge K sorted, median stream | "Kth largest/smallest", "merge K", "median", "schedule" |
| `10_graphs` | BFS shortest path, DFS connectivity, Union-Find, Topo Sort, Dijkstra | "Islands", "shortest path", "course schedule", "connected components", "network delay" |

**Deliverables**: README + templates + 8-12 solved problems per module.

---

### Phase 4: Algorithmic Paradigms (Week 9-12)
> The hardest patterns. Where senior engineers are separated from juniors.

| Module | Pattern | Recognition Signals |
|--------|---------|-------------------|
| `11_backtracking` | Subsets, permutations, combinations, constraint satisfaction | "Generate all", "find all", "N-queens", "combination sum" |
| `12_dynamic_programming` | 1D DP, 2D DP, knapsack, LCS/LIS, state machine DP, interval DP | "Minimum cost", "number of ways", "can you reach", "optimal substructure + overlapping subproblems" |
| `13_greedy` | Sorting + local optimal, activity selection, jump game | "Maximum/minimum with constraint", "schedule", "jump game", "assign cookies" |
| `14_intervals` | Merge, insert, intersection, meeting rooms | "Intervals", "overlapping", "meeting rooms", "merge" |
| `15_math_and_geometry` | Modular arithmetic, GCD, geometry, number theory | "Rotate matrix", "spiral order", "power/sqrt", "prime" |

**Deliverables**: README + templates + 10-15 solved problems per module.

---

### Phase 5: Integration & Hybrid Problems (Week 13-14)
> Real FAANG problems often combine 2-3 patterns. Train on hybrids.

- BFS + DP (e.g., Word Ladder)
- Binary Search + Greedy (e.g., Split Array Largest Sum)
- Graph + Union-Find + Sorting (e.g., Accounts Merge)
- Trie + Backtracking (e.g., Word Search II)
- Heap + Two Pointers (e.g., Find Median from Data Stream)

---

### Phase 6: Mock Interviews & Spaced Repetition (Week 15+)
> Simulate real pressure. Retain everything long-term.

- 45-minute timed sessions (2 medium or 1 hard)
- Talk through solutions out loud
- Spaced repetition review cycles (details below)

---

## 🔀 The Pattern Decision Tree

> [!TIP]
> **This is the most important section.** Print this. Internalize it. When you read a problem, run through this decision tree mentally.

```
READ THE PROBLEM
       │
       ▼
┌─────────────────────────────────┐
│ What is the INPUT type?         │
└─────────────────────────────────┘
       │
       ├── Array/String ──────────────────────────────────────┐
       │      │                                                │
       │      ├── Is it SORTED? ──► Two Pointers / Binary Search
       │      │                                                │
       │      ├── Contiguous subarray/substring? ──► Sliding Window
       │      │                                                │
       │      ├── Need frequency/existence check? ──► Hash Map │
       │      │                                                │
       │      ├── "Next greater/smaller"? ──► Monotonic Stack  │
       │      │                                                │
       │      ├── Prefix/cumulative property? ──► Prefix Sum   │
       │      │                                                │
       │      └── Optimize (min/max/count ways)? ──► DP or Greedy
       │                                                       │
       ├── Linked List ───────────────────────────────────────┐
       │      │                                                │
       │      ├── Cycle? Middle? ──► Fast & Slow Pointers      │
       │      ├── Merge/Sort? ──► Dummy Head + Two Pointers    │
       │      └── Reverse? ──► Iterative reversal pattern      │
       │                                                       │
       ├── Tree ──────────────────────────────────────────────┐
       │      │                                                │
       │      ├── Level-by-level? ──► BFS (Queue)              │
       │      ├── Path/subtree? ──► DFS (Recursion)            │
       │      ├── Search/validate? ──► BST properties          │
       │      └── Prefix matching? ──► Trie                    │
       │                                                       │
       ├── Graph ─────────────────────────────────────────────┐
       │      │                                                │
       │      ├── Shortest path (unweighted)? ──► BFS          │
       │      ├── Shortest path (weighted)? ──► Dijkstra       │
       │      ├── Connectivity/components? ──► Union-Find/DFS  │
       │      ├── Ordering/dependencies? ──► Topological Sort  │
       │      └── All paths/explore all? ──► DFS/Backtracking  │
       │                                                       │
       └── General ───────────────────────────────────────────┐
              │                                                │
              ├── "Generate ALL" / "Find ALL"? ──► Backtracking│
              ├── "Top K" / "Kth"? ──► Heap                    │
              ├── Intervals? ──► Sort + Merge/Sweep Line       │
              ├── Optimization + overlapping subproblems? ──► DP
              └── Local choice = global optimal? ──► Greedy    │
```

---

## 📋 Curated Problem Sets Per Module

> [!NOTE]
> Each module contains carefully selected problems ordered by difficulty. The goal is **not** to solve all of LeetCode — it's to deeply understand **~150-180 problems** that cover every pattern variation you'll ever encounter.

### Approximate Problem Distribution

| Module | Easy | Medium | Hard | Total |
|--------|------|--------|------|-------|
| Arrays & Hashing | 3 | 6 | 2 | 11 |
| Two Pointers | 2 | 5 | 1 | 8 |
| Sliding Window | 1 | 4 | 2 | 7 |
| Binary Search | 1 | 5 | 2 | 8 |
| Stacks & Queues | 2 | 5 | 2 | 9 |
| Linked Lists | 2 | 4 | 1 | 7 |
| Trees | 3 | 7 | 2 | 12 |
| Tries | 0 | 2 | 1 | 3 |
| Heaps | 1 | 3 | 2 | 6 |
| Graphs | 2 | 7 | 3 | 12 |
| Backtracking | 1 | 5 | 2 | 8 |
| Dynamic Programming | 2 | 8 | 5 | 15 |
| Greedy | 2 | 4 | 1 | 7 |
| Intervals | 1 | 4 | 1 | 6 |
| Math & Geometry | 2 | 3 | 1 | 6 |
| **TOTAL** | | | | **~125-150** |

---

## 🔄 Spaced Repetition System

> [!IMPORTANT]
> **This is how you remember everything even when you wake up at 3 AM.**

### The Review Protocol

After solving each problem, rate your confidence:

| Rating | Meaning | Next Review |
|--------|---------|-------------|
| 🟢 **Instant** | Solved optimally in <10 min | Review in 2 weeks |
| 🟡 **Struggled** | Got it but took hints or >20 min | Review in 3 days |
| 🔴 **Failed** | Couldn't solve without solution | Review tomorrow, then in 3 days |

### What to Record Per Problem

```markdown
## Problem: [Name] (LC #XXX)
- **Pattern**: [e.g., Sliding Window - Variable]
- **Key Insight**: [The ONE sentence that unlocks the solution]
- **Recognition Signal**: [What in the problem told you to use this pattern]
- **Complexity**: Time O(?), Space O(?)
- **My Confidence**: 🟢/🟡/🔴
- **Review Dates**: [date1] → [date2] → [date3]
```

### Daily Practice Structure

| Time | Activity |
|------|----------|
| **15 min** | Review 2-3 problems from your spaced repetition queue (solve from scratch) |
| **45 min** | Learn new pattern / solve 1-2 new problems with deep annotation |
| **15 min** | Update tracker, write key insights, rate confidence |

---

## 📂 Each Module README Format

Every `README.md` in each module folder follows this structure:

```markdown
# [Pattern Name]

## 🎯 When to Use This Pattern
- Signal words and phrases to look for in problem statements
- Input/output characteristics that suggest this pattern

## 🧠 Core Concept
- Plain English explanation of why/how this pattern works
- Visual diagrams where helpful

## 📐 Template Code (Python)
- The generic skeleton you can adapt to any problem of this type
- Annotated line-by-line

## ⚡ Variations
- Sub-patterns within this category
- How to modify the template for each variation

## 🏋️ Practice Problems (Ordered by Difficulty)
- Problem links with difficulty tags
- Brief hint for each (what makes it unique)

## 🔗 Related Patterns
- How this pattern connects to others
- Common hybrid combinations
```

---

## User Review Required

> [!IMPORTANT]
> **Please review and provide feedback on the following before I begin building:**

1. **Scope**: Is the 15-module structure with ~150 problems the right scope? Would you prefer fewer modules for a faster start, or is comprehensive coverage important?

2. **Depth per module**: Each module will have a README (pattern guide), templates.py (reusable code), and a problems/ folder. Is this the right level of detail?

3. **Timeline**: The plan assumes ~15 weeks at ~1-1.5 hours/day. Does this timeline work for you, or do you need a compressed/expanded version?

4. **Starting point**: Should I start building from Phase 1 (Foundations) and go in order, or would you prefer me to start with a specific module you find most challenging?

5. **Problem format**: For each solved problem, I'll include: the problem statement summary, recognition signals, step-by-step approach, clean Python solution with comments, complexity analysis, and key takeaways. Is there anything else you'd want per problem?

## Open Questions

> [!NOTE]
> - Are you preparing for a specific interview timeline, or is this a long-term skill-building effort?
> - Do you have any particular weak areas (e.g., DP, Graphs) you'd like extra focus on?
> - Would you like me to also include a `python_tricks.py` file with interview-specific Python idioms (e.g., `defaultdict`, `bisect`, `heapq` patterns)?

## Verification Plan

### Automated Tests
- Each `templates.py` will include runnable doctests/assertions to verify correctness
- Each problem solution will have test cases that can be run via `python -m pytest` or direct execution

### Manual Verification
- You solve problems using only the templates and decision tree (no peeking at solutions)
- Track hit-rate: "% of problems where the decision tree pointed to the correct pattern on first try"
- Goal: **>90% pattern recognition accuracy** within 8 weeks
