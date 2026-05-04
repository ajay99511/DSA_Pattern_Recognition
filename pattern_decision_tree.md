# 🔀 Pattern Decision Tree — The Master Flowchart

> **How to use**: Read a problem → run through this tree top-to-bottom → identify the pattern in <60 seconds.
> Print this. Tape it to your wall. Internalize it until it's automatic.

---

## Step 0: Read the Constraints First

Before anything else, check `N` (input size). This tells you the **maximum complexity** your solution can afford:

| Constraint | Max Complexity | Likely Patterns |
|-----------|---------------|----------------|
| N ≤ 10-12 | O(N! or 2^N) | Backtracking, Bitmask DP |
| N ≤ 20-25 | O(2^N × N) | Bitmask DP, Backtracking with pruning |
| N ≤ 100 | O(N³) | 2D DP, Floyd-Warshall |
| N ≤ 1,000 | O(N²) | 2D DP, Nested loops |
| N ≤ 100,000 | O(N log N) | Sorting, Binary Search, Heap, Merge Sort |
| N ≤ 1,000,000 | O(N) | Hash Map, Two Pointers, Sliding Window, Prefix Sum |
| N ≤ 10^9 | O(log N) or O(1) | Binary Search on answer, Math |

---

## Step 1: Identify the Input Type

```
┌─────────────────────────────────────────────────┐
│            What is the PRIMARY input?            │
└─────────────────────────────────────────────────┘
         │
         ├── Array / String ──────────────── Go to §2
         ├── Linked List ─────────────────── Go to §3
         ├── Tree ────────────────────────── Go to §4
         ├── Graph / Grid / Matrix ───────── Go to §5
         ├── Intervals / Ranges ──────────── Go to §6
         └── Number / Math / General ─────── Go to §7
```

---

## §2: Array / String Problems

```
Is the array SORTED (or can be sorted without losing info)?
  │
  ├── YES ─┬── Need to find a pair/triplet? ──────► TWO POINTERS
  │        ├── Need to find a target/boundary? ───► BINARY SEARCH
  │        └── Need to merge two sorted things? ──► TWO POINTERS / MERGE
  │
  └── NO ──┬── Need subarray/substring (contiguous)? ─┐
           │    │                                       │
           │    ├── Fixed size window? ────────────► SLIDING WINDOW (Fixed)
           │    ├── Variable size + condition? ────► SLIDING WINDOW (Variable)
           │    └── Subarray sum = K? ────────────► PREFIX SUM + HASH MAP
           │
           ├── Need frequency / existence / duplicates?
           │    └──────────────────────────────────► HASH MAP / HASH SET
           │
           ├── "Next greater" / "Next smaller" / "Previous greater"?
           │    └──────────────────────────────────► MONOTONIC STACK
           │
           ├── Need cumulative/running aggregate?
           │    └──────────────────────────────────► PREFIX SUM / PREFIX PRODUCT
           │
           ├── Need to optimize (min cost, max profit, # of ways)?
           │    ├── Overlapping subproblems? ──────► DYNAMIC PROGRAMMING
           │    └── Greedy choice works? ──────────► GREEDY
           │
           ├── "Generate ALL" / "Find ALL combinations"?
           │    └──────────────────────────────────► BACKTRACKING
           │
           └── Need top K / Kth element?
                └──────────────────────────────────► HEAP (or Quickselect)
```

### Signal Words for Array/String:
| Signal | Pattern |
|--------|---------|
| "sorted array", "two sum" | Two Pointers |
| "maximum subarray", "substring", "contiguous" | Sliding Window |
| "subarray sum equals K" | Prefix Sum + Hash Map |
| "anagram", "frequency", "duplicate" | Hash Map |
| "daily temperatures", "next greater element" | Monotonic Stack |
| "longest increasing subsequence" | DP (or patience sorting) |
| "minimum window substring" | Sliding Window + Hash Map |

---

## §3: Linked List Problems

```
┌─────────────────────────────────────────┐
│         What does the problem ask?       │
└─────────────────────────────────────────┘
  │
  ├── Detect cycle / Find cycle start? ──────────► FAST & SLOW POINTERS
  ├── Find middle element? ──────────────────────► FAST & SLOW POINTERS
  ├── Find Nth from end? ────────────────────────► TWO POINTERS (gap N)
  ├── Reverse (whole or partial)? ───────────────► ITERATIVE 3-POINTER REVERSAL
  ├── Merge two sorted lists? ──────────────────► DUMMY HEAD + COMPARISON
  ├── Merge K sorted lists? ────────────────────► HEAP + DUMMY HEAD
  ├── Reorder / Rearrange? ─────────────────────► FIND MIDDLE + REVERSE + MERGE
  └── Palindrome check? ────────────────────────► FIND MIDDLE + REVERSE + COMPARE
```

---

## §4: Tree Problems

```
┌─────────────────────────────────────────┐
│         What does the problem ask?       │
└─────────────────────────────────────────┘
  │
  ├── Level-by-level processing? ────────────────► BFS (Queue)
  │     Examples: level order traversal, minimum depth,
  │     right side view, zigzag traversal
  │
  ├── Path from root / subtree property? ────────► DFS (Recursion)
  │     Examples: max depth, path sum, diameter,
  │     lowest common ancestor, subtree checks
  │
  ├── Search / Validate / Insert in BST? ────────► BST PROPERTIES
  │     Key: left < node < right
  │     Use in-order traversal for sorted order
  │
  ├── Serialize / Deserialize? ──────────────────► BFS or PREORDER DFS
  │
  └── Word/prefix lookup in dictionary? ─────────► TRIE (go to §4b)
```

### §4b: Trie Problems
```
  ├── "Starts with" / "Prefix match"? ──────────► TRIE
  ├── "Word dictionary with wildcards"? ────────► TRIE + DFS
  └── "Word search in grid"? ───────────────────► TRIE + BACKTRACKING
```

### Tree DFS Return Patterns (Critical):
| What to return | Example |
|---------------|---------|
| Boolean (is valid?) | Validate BST, symmetric tree |
| Integer (height/depth/sum) | Max depth, diameter, path sum |
| Node reference | LCA, inorder successor |
| List/accumulator | All paths, boundary traversal |

---

## §5: Graph / Grid / Matrix Problems

```
┌─────────────────────────────────────────┐
│         What does the problem ask?       │
└─────────────────────────────────────────┘
  │
  ├── Shortest path (unweighted)? ───────────────► BFS
  │     Examples: shortest path in maze, word ladder,
  │     rotting oranges (multi-source BFS)
  │
  ├── Shortest path (weighted, non-negative)? ──► DIJKSTRA
  │
  ├── Shortest path (negative weights)? ────────► BELLMAN-FORD
  │
  ├── All-pairs shortest path? ─────────────────► FLOYD-WARSHALL
  │
  ├── Connected components / Islands? ──────────► DFS or BFS or UNION-FIND
  │
  ├── Cycle detection?
  │     ├── Directed graph? ────────────────────► DFS with 3 colors (white/gray/black)
  │     └── Undirected graph? ──────────────────► UNION-FIND or DFS with parent tracking
  │
  ├── Ordering / Dependencies / Prerequisites? ─► TOPOLOGICAL SORT (Kahn's BFS)
  │     Examples: course schedule, build order,
  │     alien dictionary
  │
  ├── Minimum Spanning Tree? ───────────────────► KRUSKAL'S (Union-Find) or PRIM'S
  │
  ├── "Can I reach?" / Connectivity? ───────────► UNION-FIND or DFS
  │
  └── Explore ALL paths / states? ──────────────► DFS + BACKTRACKING
```

### Grid-Specific Signals:
| Signal | Pattern |
|--------|---------|
| "Number of islands" | DFS/BFS flood fill |
| "Shortest path in grid" | BFS |
| "Rotting oranges" / "Walls and gates" | Multi-source BFS |
| "Surrounded regions" | DFS from border |

---

## §6: Interval Problems

```
┌─────────────────────────────────────────┐
│   Does the problem involve intervals?    │
└─────────────────────────────────────────┘
  │
  ├── Merge overlapping intervals? ─────────────► SORT by start + MERGE
  ├── Insert a new interval? ───────────────────► SORT + LINEAR SCAN
  ├── Find max overlapping / meeting rooms? ────► SORT + SWEEP LINE (or MIN HEAP)
  ├── Find intersection of two lists? ──────────► TWO POINTERS
  └── Find gaps between intervals? ─────────────► SORT + COMPARE consecutive
```

**Always sort intervals by start time first** (or by end time for activity selection).

---

## §7: General / Optimization Problems

```
┌─────────────────────────────────────────┐
│      What is the problem asking for?     │
└─────────────────────────────────────────┘
  │
  ├── "MINIMUM cost / MAXIMUM profit / # of WAYS"
  │     ├── Can I make a local choice that's always optimal?
  │     │     └── YES ──────────────────────────► GREEDY
  │     └── Do I need to consider all possibilities?
  │           └── YES (overlapping subproblems) ► DYNAMIC PROGRAMMING
  │
  ├── "Generate ALL permutations / combinations / subsets"
  │     └──────────────────────────────────────► BACKTRACKING
  │
  ├── "Top K" / "Kth largest" / "K most frequent"
  │     └──────────────────────────────────────► HEAP (Min or Max)
  │
  ├── "Median from data stream"
  │     └──────────────────────────────────────► TWO HEAPS (max + min)
  │
  ├── "Design a data structure"
  │     └── Usually combines: HASH MAP + LINKED LIST / HEAP / TREE
  │
  └── Bit-level operations / Single number?
        └──────────────────────────────────────► BIT MANIPULATION (XOR tricks)
```

---

## DP Sub-Pattern Decision Tree

When you know it's DP, narrow further:

```
┌──────────────────────────────────────┐
│     What's the DP state about?        │
└──────────────────────────────────────┘
  │
  ├── Linear sequence (1D)?
  │     ├── "Climbing stairs" / "House robber" ──► dp[i] = f(dp[i-1], dp[i-2])
  │     ├── "Coin change" / "Perfect squares" ──► dp[amount] = min over choices
  │     └── "Word break" / "Decode ways" ────────► dp[i] = sum of valid splits
  │
  ├── Two sequences / Grid (2D)?
  │     ├── "Edit distance" / "LCS" ─────────────► dp[i][j] on two strings
  │     ├── "Unique paths" / "Min path sum" ─────► dp[row][col] on grid
  │     └── "Interleaving string" ───────────────► dp[i][j] matching positions
  │
  ├── Knapsack-type?
  │     ├── "Subset sum" / "Partition equal" ────► dp[i][capacity] with include/exclude
  │     ├── "Coin change (count ways)" ──────────► Unbounded knapsack
  │     └── "Target sum with +/-" ───────────────► Offset-based DP or knapsack transform
  │
  ├── Interval-based?
  │     ├── "Burst balloons" / "Matrix chain" ──► dp[i][j] = best over split point k
  │     └── "Palindrome partitioning" ──────────► dp[i][j] = is substring palindrome?
  │
  ├── State machine?
  │     ├── "Best time buy/sell stock" series ──► States: hold / not_hold / cooldown
  │     └── "Paint house" / "Decode ways II" ──► States: last_choice made
  │
  ├── Tree DP?
  │     ├── "House robber III" ──────────────────► DFS returns (rob, skip) tuple
  │     └── "Diameter of binary tree" ──────────► DFS returns depth, tracks global max
  │
  └── Bitmask DP? (N ≤ 20)
        ├── "Shortest path visiting all nodes" ─► dp[mask][node]
        └── "Assign tasks to workers" ──────────► dp[mask] = min cost
```

---

## Quick-Reference Cheat Card

| I see... | I think... |
|----------|-----------|
| Sorted array + find pair | Two Pointers |
| Unsorted + find pair/existence | Hash Map |
| Contiguous subarray/substring | Sliding Window |
| Subarray sum = K | Prefix Sum + Hash Map |
| Sorted + find boundary/target | Binary Search |
| "Find minimum that satisfies X" | Binary Search on Answer |
| Next greater/smaller element | Monotonic Stack |
| Linked list + cycle/middle | Fast & Slow Pointers |
| Tree + level processing | BFS |
| Tree + path/depth/validation | DFS |
| Graph + shortest path (unweighted) | BFS |
| Graph + shortest path (weighted) | Dijkstra |
| Graph + components | Union-Find or DFS |
| Graph + ordering | Topological Sort |
| Overlapping intervals | Sort + Merge |
| "Generate all" / exhaustive search | Backtracking |
| Optimization + overlapping subproblems | DP |
| Local choice = global optimal | Greedy |
| Top K / Kth element | Heap |
| Median from stream | Two Heaps |
| N ≤ 20 + visit all states | Bitmask DP |
| Range query with updates | Segment Tree |
| XOR / single number / bit tricks | Bit Manipulation |
