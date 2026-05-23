# ⏱️ Complexity Cheatsheet — One-Page Reference

## Time Complexity Rankings (Best → Worst)

| Notation | Name | Example | At N=10^6 |
|----------|------|---------|-----------|
| O(1) | Constant | Hash map lookup, array index | 1 op |
| O(log N) | Logarithmic | Binary search | 20 ops |
| O(√N) | Square root | Prime check, sqrt decomposition | 1,000 ops |
| O(N) | Linear | Single pass, two pointers | 10^6 ops |
| O(N log N) | Linearithmic | Merge sort, heap sort | 2×10^7 ops |
| O(N²) | Quadratic | Nested loops, bubble sort | 10^12 ops ❌ |
| O(N³) | Cubic | Floyd-Warshall, 3D DP | 10^18 ops ❌ |
| O(2^N) | Exponential | Subsets, backtracking | 10^301030 ❌ |
| O(N!) | Factorial | Permutations | ∞ ❌ |

> ❌ = Will TLE for N = 10^6. Safe rule: **≤ 10^8 operations per second**.

---

## Data Structure Operations

| Structure | Access | Search | Insert | Delete | Notes |
|-----------|--------|--------|--------|--------|-------|
| Array | O(1) | O(N) | O(N) | O(N) | O(1) append amortized |
| Linked List | O(N) | O(N) | O(1)* | O(1)* | *If you have the node |
| Hash Map/Set | — | O(1) avg | O(1) avg | O(1) avg | O(N) worst case |
| BST (balanced) | — | O(log N) | O(log N) | O(log N) | Python: `SortedList` |
| Heap | O(1) top | O(N) | O(log N) | O(log N) | Python: `heapq` |
| Stack/Queue | O(1) top | O(N) | O(1) | O(1) | — |
| Trie | — | O(L) | O(L) | O(L) | L = word length |
| Segment Tree | — | O(log N) | O(log N) | O(log N) | Range queries |
| Union-Find | — | O(α(N))≈O(1) | O(α(N))≈O(1) | — | With path compression |

---

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable? | Notes |
|-----------|------|---------|-------|-------|---------|-------|
| Python `sort()` | O(N log N) | O(N log N) | O(N log N) | O(N) | ✅ Yes | Timsort (hybrid merge+insertion) |
| Bubble Sort | O(N) | O(N²) | O(N²) | O(1) | ✅ Yes | Best case: already sorted |
| Selection Sort | O(N²) | O(N²) | O(N²) | O(1) | ❌ No | Always N² — never use in practice |
| Insertion Sort | O(N) | O(N²) | O(N²) | O(1) | ✅ Yes | Fast for nearly-sorted / small N |
| Merge Sort | O(N log N) | O(N log N) | O(N log N) | O(N) | ✅ Yes | Guaranteed O(N log N), extra space |
| Quick Sort | O(N log N) | O(N log N) | O(N²) | O(log N) | ❌ No | Worst case on sorted input w/o pivot randomization |
| Heap Sort | O(N log N) | O(N log N) | O(N log N) | O(1) | ❌ No | In-place, but poor cache performance |
| Counting Sort | O(N+K) | O(N+K) | O(N+K) | O(K) | ✅ Yes | K = value range; integers only |
| Radix Sort | O(d×(N+K)) | O(d×(N+K)) | O(d×(N+K)) | O(N+K) | ✅ Yes | d = digits, K = base (10 or 256) |

---

## Algorithm Complexities

### Graph Algorithms
| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| BFS | O(V+E) | O(V) | Shortest path (unweighted) |
| DFS | O(V+E) | O(V) | Connectivity, cycle detection |
| Dijkstra (min-heap) | O((V+E) log V) | O(V) | Shortest path (weighted, non-neg) |
| Bellman-Ford | O(V×E) | O(V) | Shortest path (negative weights) |
| Floyd-Warshall | O(V³) | O(V²) | All-pairs shortest path |
| Kruskal's MST | O(E log E) | O(V) | Minimum spanning tree |
| Topological Sort | O(V+E) | O(V) | Dependency ordering |

### DP Common Patterns
| Pattern | Time | Space | Optimizable? |
|---------|------|-------|-------------|
| 1D (linear) | O(N) | O(N) | → O(1) with rolling variables |
| 2D (grid/string) | O(N×M) | O(N×M) | → O(min(N,M)) with rolling row |
| Knapsack | O(N×W) | O(N×W) | → O(W) with 1D array |
| LIS | O(N²) | O(N) | → O(N log N) with patience sort |
| Bitmask DP | O(2^N × N) | O(2^N) | Only for N ≤ 20 |

### Binary Search Variants
| Variant | Key Difference |
|---------|---------------|
| Find exact target | `if nums[mid] == target: return mid` |
| Find leftmost (lower bound) | `if nums[mid] >= target: right = mid` |
| Find rightmost (upper bound) | `if nums[mid] <= target: left = mid` |
| Search on answer | Search the answer space, not the array |

---

## Python-Specific Complexity Notes

```python
# LIST operations
list.append(x)        # O(1) amortized — fast
list.pop()            # O(1) — remove from end
list[i]               # O(1) — index access
list.insert(0, x)     # O(N) ❌ shifts everything — use deque
list.pop(0)           # O(N) ❌ shifts everything — use deque.popleft()
x in list             # O(N) ❌ linear scan — use set
list.remove(x)        # O(N) ❌ linear scan
list.sort()           # O(N log N) — Timsort, in-place
sorted(list)          # O(N log N) — returns new list

# DICT operations
dict[key]             # O(1) avg — hash lookup
dict[key] = val       # O(1) avg — hash insert
del dict[key]         # O(1) avg — hash delete
key in dict           # O(1) avg — hash membership
dict.items()          # O(1) — returns view (not a copy)

# SET operations
set.add(x)            # O(1) avg
set.remove(x)         # O(1) avg
x in set              # O(1) avg ✅ use instead of `x in list`
set1 & set2           # O(min(len(s1), len(s2))) — intersection
set1 | set2           # O(len(s1) + len(s2)) — union

# HEAPQ (min-heap only — negate values for max-heap)
heapq.heappush(h, x)  # O(log N)
heapq.heappop(h)      # O(log N) — removes/returns smallest
heapq.heapify(list)   # O(N) — build heap in-place
h[0]                  # O(1) — peek min without removing
heapq.nlargest(k, h)  # O(N log k)
heapq.nsmallest(k, h) # O(N log k)

# DEQUE (collections.deque — use for BFS queues)
deque.append(x)       # O(1) — add to right
deque.appendleft(x)   # O(1) — add to left
deque.pop()           # O(1) — remove from right
deque.popleft()       # O(1) ✅ use instead of list.pop(0)
x in deque            # O(N) — still linear scan
```

---

## Quick Constraint → Algorithm Mapping

```
N ≤ 12     → Brute force / Backtracking / Bitmask DP    → O(2^N) or O(N!)
N ≤ 20     → Bitmask DP                                  → O(2^N × N)
N ≤ 100    → O(N³) DP, Floyd-Warshall                    → O(N³)
N ≤ 1,000  → O(N²) DP, nested loops                      → O(N²)
N ≤ 10^5   → Sorting, Binary Search, Heap, BFS/DFS       → O(N log N)
N ≤ 10^6   → Hash Map, Two Pointers, Sliding Window      → O(N)
N ≤ 10^9   → Binary Search on answer, Math                → O(log N)
N ≤ 10^18  → Math formula, matrix exponentiation          → O(log N)
```
