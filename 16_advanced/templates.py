"""Advanced — Bitmask DP, Segment Tree, Fenwick Tree"""
from typing import List
from collections import deque


# ============================================================
# BITMASK DP
# ============================================================

def shortest_path_all_nodes(graph: List[List[int]]) -> int:
    """LC #847 — BFS + bitmask. Visit all nodes shortest path."""
    n = len(graph)
    full = (1 << n) - 1
    queue = deque()
    visited = set()
    for i in range(n):
        state = (1 << i, i)
        queue.append((state[0], state[1], 0))
        visited.add(state)
    while queue:
        mask, node, dist = queue.popleft()
        if mask == full:
            return dist
        for nei in graph[node]:
            new_mask = mask | (1 << nei)
            if (new_mask, nei) not in visited:
                visited.add((new_mask, nei))
                queue.append((new_mask, nei, dist + 1))
    return -1


# ============================================================
# SEGMENT TREE (Iterative, bottom-up)
# ============================================================

class SegmentTree:
    """Range sum queries with point updates. O(log N) per operation."""
    
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def update(self, i: int, val: int):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def query(self, l: int, r: int) -> int:
        """Sum of [l, r) — half-open interval."""
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res


# ============================================================
# FENWICK TREE (Binary Indexed Tree)
# ============================================================

class FenwickTree:
    """Prefix sums with point updates. Simpler than Segment Tree."""
    
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i: int, delta: int = 1):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    
    def query(self, i: int) -> int:
        """Prefix sum [0, i]."""
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    
    def range_query(self, l: int, r: int) -> int:
        """Sum of [l, r]."""
        return self.query(r) - (self.query(l - 1) if l > 0 else 0)


def count_smaller_after_self(nums: List[int]) -> List[int]:
    """LC #315 — Using BIT with coordinate compression."""
    sorted_unique = sorted(set(nums))
    rank = {v: i for i, v in enumerate(sorted_unique)}
    n = len(sorted_unique)
    bit = FenwickTree(n)
    result = []
    for num in reversed(nums):
        r = rank[num]
        result.append(bit.query(r - 1) if r > 0 else 0)
        bit.update(r)
    return result[::-1]


if __name__ == "__main__":
    # Segment Tree
    st = SegmentTree([1, 3, 5, 7, 9, 11])
    assert st.query(1, 4) == 15  # 3 + 5 + 7
    st.update(2, 10)             # Change 5 → 10
    assert st.query(1, 4) == 20  # 3 + 10 + 7
    
    # Fenwick Tree
    ft = FenwickTree(5)
    ft.update(0, 1); ft.update(1, 3); ft.update(2, 5)
    assert ft.query(2) == 9  # 1 + 3 + 5
    assert ft.range_query(1, 2) == 8  # 3 + 5
    
    # Count Smaller
    assert count_smaller_after_self([5, 2, 6, 1]) == [2, 1, 1, 0]
    
    print("✅ All advanced templates passed!")
