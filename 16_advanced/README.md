# Advanced — L5/L6 Level

## 🎯 What Separates Senior from Mid-Level
These patterns appear in Google/Meta hard rounds and distinguish L5/L6 candidates.

## Sub-Pattern 1: Bitmask DP
**When**: N ≤ 20, need to track "which items are used/visited"
**State**: `dp[mask]` where `mask` is a bitmask of N items
**Signal words**: "visit all nodes", "assign tasks", "traveling salesman", small N

### Template
```python
def shortest_path_all_nodes(graph):
    n = len(graph)
    # dp[mask][node] = shortest path visiting nodes in mask, ending at node
    dp = [[float('inf')] * n for _ in range(1 << n)]
    queue = deque()
    for i in range(n):
        dp[1 << i][i] = 0
        queue.append((1 << i, i))
    full_mask = (1 << n) - 1
    while queue:
        mask, node = queue.popleft()
        if mask == full_mask: return dp[mask][node]
        for nei in graph[node]:
            new_mask = mask | (1 << nei)
            if dp[new_mask][nei] > dp[mask][node] + 1:
                dp[new_mask][nei] = dp[mask][node] + 1
                queue.append((new_mask, nei))
```

## Sub-Pattern 2: Segment Tree
**When**: Range queries (sum/min/max) WITH point or range updates
**Signal**: "range sum query with updates", "count inversions"

### Template
```python
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    
    def query(self, l, r):  # [l, r) sum
        res = 0
        l += self.n; r += self.n
        while l < r:
            if l & 1: res += self.tree[l]; l += 1
            if r & 1: r -= 1; res += self.tree[r]
            l //= 2; r //= 2
        return res
```

## Sub-Pattern 3: Fenwick Tree (Binary Indexed Tree)
**When**: Prefix sums with point updates — simpler than Segment Tree
**Signal**: "dynamic prefix sum", "count smaller numbers after self"

### Template
```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta=1):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    
    def query(self, i):  # prefix sum [0, i]
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    
    def range_query(self, l, r):
        return self.query(r) - (self.query(l-1) if l > 0 else 0)
```

## 🏋️ Practice Problems
| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #847 Shortest Path Visiting All | Hard | BFS + Bitmask state |
| 2 | LC #1125 Smallest Sufficient Team | Hard | Bitmask DP on skills |
| 3 | LC #943 Shortest Superstring | Hard | Bitmask DP + overlap |
| 4 | LC #307 Range Sum Query Mutable | Medium | Segment Tree or BIT |
| 5 | LC #315 Count Smaller After Self | Hard | BIT or merge sort |
| 6 | LC #218 The Skyline Problem | Hard | Sweep line + heap |
| 7 | LC #327 Count Range Sum | Hard | Merge sort or BIT |
| 8 | LC #1584 Min Cost Connect Points | Medium | MST (Kruskal's + UF) |
| 9 | LC #2421 Max Points From Grid | Hard | Bitmask DP on columns |
