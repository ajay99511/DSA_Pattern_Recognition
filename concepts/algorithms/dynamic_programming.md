# Dynamic Programming: The Art of Storing State

## 1. Space Optimization: The "Sliding Variable" Schematic
In many DP problems, you don't need the entire $O(n)$ table. You only need the previous 1 or 2 states.

### Schematic: Fibonacci Optimization
```mermaid
graph LR
    subgraph Iteration_N [Calculate F(n)]
    P1[Prev2] --- P2[Prev1] --- C[Current]
    end
    
    subgraph Iteration_N1 [Calculate F(n+1)]
    NP1[Prev1] --- NP2[Current] --- NC[New Current]
    end
    
    Iteration_N -- "Shift Pointers" --> Iteration_N1
    
    style C fill:#f9f
    style NC fill:#6f9
```
**Result**: Space reduced from $O(n)$ to $O(1)$.

---

## 2. DP on Grids: The "Flow" Schematic

### Conceptual Overview
Finding the "Minimum Path Sum" from $(0,0)$ to $(n,m)$. You can only move Right or Down.

### Schematic: Transition Logic
```mermaid
graph TD
    subgraph Matrix
    direction TB
    C1[Target: i, j]
    C2[From Top: i-1, j]
    C3[From Left: i, j-1]
    
    C2 --> C1
    C3 --> C1
    end
    
    Logic["dp[i][j] = val[i][j] + min(dp[i-1][j], dp[i][j-1])"]
    
    style C1 fill:#6f9
```

---

## 3. String DP: Longest Common Subsequence (LCS)

### Schematic: State Transition Matrix
```mermaid
graph TD
    subgraph Matrix_LCS [String A: 'ABC', String B: 'ACE']
    direction TB
    M[0 0 0 0<br>0 1 1 1<br>0 1 1 1<br>0 1 1 2]
    end
    
    Diagonal["If A[i] == B[j]: dp[i][j] = 1 + dp[i-1][j-1]"]
    Straight["Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])"]
    
    style Matrix_LCS fill:#eee
```

---

## 4. Advanced Sub-Topics

### Bitmask DP
Using a bitmask to represent a "set" of used items.
- **Complexity**: $O(2^n \cdot n)$.
- **Use Case**: Traveling Salesperson Problem (TSP).

### Interval DP
Solving subproblems defined by a range $[i, j]$.
- **Complexity**: $O(n^3)$.
- **Use Case**: Matrix Chain Multiplication, Burst Balloons.

---

## 5. Developer Cheat Sheet

| DP Pattern | Strategy | Example Problem |
| :--- | :--- | :--- |
| **0/1 Knapsack** | Pick / Don't Pick | Target Sum |
| **Unbounded Knapsack**| Infinite Supply | Coin Change |
| **Grid DP** | Move Right/Down | Unique Paths |
| **String DP** | Match / No Match | Edit Distance |

### Critical Patterns
- **Identify Substructure**: Does the answer to $n$ depend on $n-1, n-2, \dots$?
- **Iterative > Recursive**: Avoid recursion depth limits and stack overhead.
- **Base Cases**: Always define $dp[0]$ or $dp[0][0]$ first.
