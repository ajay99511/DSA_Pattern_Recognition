# 🔧 Problem Decomposition Protocol

> **When to use**: When a problem doesn't fit cleanly into ONE pattern — which is most FAANG hard problems.

---

## The 4-Step Protocol

### Step 1: IDENTIFY THE LAYERS

Read the problem carefully. Ask yourself:

> "Is this ONE pattern, or does it have STAGES?"

**Most hard problems have 2-3 stages:**
- "Preprocess" + "Query"
- "Build" + "Search"  
- "Transform" + "Optimize"
- "Sort/Group" + "Process each group"

**How to spot layers:**
- Multiple distinct operations mentioned in the problem
- "Given X, find Y" where X needs processing before you can find Y
- The brute force has clearly separable expensive parts

### Step 2: DECOMPOSE INTO SUB-PROBLEMS

For each stage, independently ask: **"What pattern solves THIS piece?"**

Use the Pattern Decision Tree on each sub-problem separately.

**Example decompositions:**

| Problem | Stage 1 | Stage 2 | Stage 3 |
|---------|---------|---------|---------|
| Word Search II | Build Trie from words | Backtrack on grid using Trie | — |
| Accounts Merge | Build graph from emails | DFS/Union-Find components | Sort & format output |
| Split Array Largest Sum | Binary search on answer | Greedy validation check | — |
| Median from Data Stream | Insert into two heaps | Balance heaps | Query median |
| LRU Cache | Hash Map for O(1) lookup | Doubly Linked List for O(1) eviction | — |
| Cheapest Flights ≤ K Stops | Model as graph | BFS/Bellman-Ford with K constraint | — |
| Sliding Window Maximum | Process array | Monotonic deque for max tracking | — |
| Count of Smaller Numbers After Self | Merge sort | Track inversions during merge | — |

### Step 3: IDENTIFY THE GLUE

The hardest part. Ask:

> "How do the stages CONNECT? What data flows between them?"

**Common glue patterns:**
- **Stage 1 builds a data structure** that Stage 2 queries
  - Example: Trie built → Backtracking uses Trie for pruning
- **Stage 1 transforms the problem** into a form Stage 2 can solve
  - Example: Binary search picks a target → Greedy validates if achievable
- **Stage 1 sorts/groups** → Stage 2 processes each group
  - Example: Sort intervals → Sweep line processes in order
- **Stages alternate per element**
  - Example: For each element, do X (stage 1) then update Y (stage 2)

### Step 4: VERIFY COMPLEXITY

Multiply the complexities of each stage:

```
Total = Complexity(Stage1) + Complexity(Stage2) + ...
      (addition if sequential, multiplication if nested)
```

**Red flag**: If total exceeds what N allows, one stage needs optimization.

**Example**:
- Word Search II: Trie build = O(total_chars), Grid backtrack = O(M×N×4^L)
- Total fits within constraints ✓

---

## Practice: Decomposition Drills

For each problem below, practice identifying the layers BEFORE coding:

### Drill Set (10 problems)

1. **Word Search II** (LC #212) — Hard
   - Layers: Trie + Backtracking
   - Glue: Trie provides pruning during grid DFS

2. **Find Median from Data Stream** (LC #295) — Hard
   - Layers: Two Heaps (max-heap + min-heap)
   - Glue: Balance invariant between heaps after each insert

3. **Accounts Merge** (LC #721) — Medium
   - Layers: Graph construction + Union-Find + Sort
   - Glue: Union-Find groups emails, then collect & sort per group

4. **Split Array Largest Sum** (LC #410) — Hard
   - Layers: Binary Search on Answer + Greedy Validation
   - Glue: Binary search picks candidate → greedy checks feasibility

5. **Largest Rectangle in Histogram** (LC #84) — Hard
   - Layers: Monotonic Stack + Width Calculation
   - Glue: Stack gives boundaries, multiply height × width

6. **Word Ladder** (LC #127) — Hard
   - Layers: Preprocessing (wildcard patterns) + BFS
   - Glue: Wildcard map enables O(1) neighbor lookup for BFS

7. **LRU Cache** (LC #146) — Medium
   - Layers: Hash Map + Doubly Linked List
   - Glue: Map stores key→node, list maintains recency order

8. **Cheapest Flights Within K Stops** (LC #787) — Medium
   - Layers: Graph + Modified Bellman-Ford/BFS
   - Glue: K constraint limits relaxation rounds

9. **Count of Smaller Numbers After Self** (LC #315) — Hard
   - Layers: Merge Sort + Inversion Counting (or Segment Tree)
   - Glue: During merge, count cross-inversions

10. **Shortest Path Visiting All Nodes** (LC #847) — Hard
    - Layers: BFS + Bitmask State
    - Glue: State = (current_node, visited_bitmask), BFS explores states

---

## Anti-Patterns: When Decomposition Goes Wrong

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| Trying to solve everything in one pass | Overcomplicates the logic, bugs everywhere | Separate into clear stages |
| Wrong stage order | Doing the expensive part first when cheap preprocessing would help | Always ask "what can I precompute?" |
| Ignoring the glue | Stages work individually but don't connect | Explicitly define the data interface between stages |
| Over-decomposing | 5+ stages when 2 would suffice | Keep it as simple as possible |
