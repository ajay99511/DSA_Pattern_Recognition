"""Graphs — Reusable Templates"""
from typing import List
from collections import deque, defaultdict
import heapq


# ============================================================
# BFS — Shortest Path (Unweighted) / Level-Order
# ============================================================

def num_islands(grid: List[List[str]]) -> int:
    """LC #200 — BFS flood fill."""
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                queue = deque([(r, c)])
                grid[r][c] = '0'
                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nr, nc = cr+dr, cc+dc
                        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1':
                            grid[nr][nc] = '0'
                            queue.append((nr, nc))
    return count


def oranges_rotting(grid: List[List[int]]) -> int:
    """LC #994 — Multi-source BFS."""
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2: queue.append((r, c, 0))
            elif grid[r][c] == 1: fresh += 1
    if fresh == 0: return 0
    time = 0
    while queue:
        r, c, t = queue.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                grid[nr][nc] = 2
                fresh -= 1
                time = t + 1
                queue.append((nr, nc, t+1))
    return time if fresh == 0 else -1


# ============================================================
# DIJKSTRA — Shortest Path (Weighted)
# ============================================================

def network_delay(times: List[List[int]], n: int, k: int) -> int:
    """LC #743."""
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    dist = {}
    heap = [(0, k)]
    while heap:
        d, node = heapq.heappop(heap)
        if node in dist: continue
        dist[node] = d
        for nei, w in graph[node]:
            if nei not in dist:
                heapq.heappush(heap, (d + w, nei))
    return max(dist.values()) if len(dist) == n else -1


# ============================================================
# UNION-FIND
# ============================================================

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        self.components -= 1
        return True


def redundant_connection(edges: List[List[int]]) -> List[int]:
    """LC #684 — Find edge that creates cycle."""
    n = len(edges)
    uf = UnionFind(n + 1)
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]
    return []


# ============================================================
# TOPOLOGICAL SORT (Kahn's BFS)
# ============================================================

def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """LC #207 — Course Schedule."""
    graph = defaultdict(list)
    indegree = [0] * numCourses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    return count == numCourses


def find_order(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """LC #210 — Course Schedule II."""
    graph = defaultdict(list)
    indegree = [0] * numCourses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    return order if len(order) == numCourses else []


if __name__ == "__main__":
    assert can_finish(2, [[1,0]]) == True
    assert can_finish(2, [[1,0],[0,1]]) == False
    assert find_order(4, [[1,0],[2,0],[3,1],[3,2]]) in [[0,1,2,3],[0,2,1,3]]
    assert redundant_connection([[1,2],[1,3],[2,3]]) == [2,3]
    
    assert network_delay([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
    
    print("✅ All graph templates passed!")
