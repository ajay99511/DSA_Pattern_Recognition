# Dynamic Programming (DP)

## 1. Conceptual Overview
**Dynamic Programming** is an optimization over plain recursion. It involves breaking a complex problem into smaller subproblems, solving each once, and storing their results.

**The Two Requirements**:
1. **Overlapping Subproblems**: The same subproblems are solved multiple times.
2. **Optimal Substructure**: The optimal solution to the problem can be built from the optimal solutions of its subproblems.

---

## 2. The DP Workflow: From Zero to Hero

### Step 1: Recursive Solution (Top-Down)
Start with a naive recursive solution.
- **Complexity**: Usually exponential (O(2ⁿ)).

### Step 2: Memoization (Top-Down + Cache)
Store the results of expensive function calls in a Hash Map or Array.
- **Complexity**: Drastically reduced to polynomial (often O(n)).

### Step 3: Tabulation (Bottom-Up)
Solve the smallest subproblems first and build up to the target using an iterative table.
- **Space Optimization**: Often, you only need the previous 1 or 2 results, allowing you to reduce space from O(n) to O(1).

---

## 3. Visual Representation: Fibonacci Example

```mermaid
graph TD
    subgraph Recursion Tree (Naive)
    F5((F5)) --> F4((F4))
    F5 --> F3((F3))
    F4 --> F3_((F3))
    F4 --> F2((F2))
    F3 --> F2_((F2))
    F3 --> F1((F1))
    end
    
    style F3_ fill:#f96,stroke:#333
    style F3 fill:#f96,stroke:#333
    style F2 fill:#6f9
    style F2_ fill:#6f9
```
*In DP, the orange nodes are calculated only once.*

---

## 4. Common DP Patterns

### 1. 0/1 Knapsack
- **Problem**: You have items with weights and values. Find the max value you can carry in a bag of capacity $W$.
- **Logic**: For each item, you either **Take** it or **Leave** it.

### 2. Unbounded Knapsack
- Similar to 0/1, but you can take multiple instances of the same item (e.g., Coin Change problem).

### 3. Longest Common Subsequence (LCS)
- Find the longest sequence that appears in both strings in the same relative order.
- **Use Case**: `git diff`, Bioinformatics.

### 4. Matrix Chain Multiplication / Interval DP
- Optimal way to multiply matrices or solve problems on a range $[i, j]$.

---

## 5. Developer Tips & Practical Knowledge

### The "State" and "Transition"
DP is all about two things:
1. **State**: What variables uniquely identify a subproblem? (e.g., `dp[i]` is the max profit up to index $i$).
2. **Transition**: How do I compute `dp[i]` from `dp[i-1]`, `dp[i-2]`, etc.?

### DP vs. Greedy
- **Greedy**: Makes the best local choice at each step (doesn't look back).
- **DP**: Considers all possible choices to find the global optimum.
- *Rule of Thumb*: If "taking the biggest" or "taking the smallest" works, it's Greedy. If you need to "try all combinations", it's DP.

### Why Bottom-Up is often better
While Memoization is more intuitive, Tabulation (Bottom-Up) avoids **Recursion Depth** limits (StackOverflowError) and is often slightly faster due to iterative performance.
