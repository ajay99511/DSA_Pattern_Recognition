# Graphs

## 🎯 When to Use
**Signal words**: "islands", "shortest path", "connected components", "course schedule", "network delay", "alien dictionary", "matrix traversal", "grid"

## 🧠 Core Decision
- **Shortest path (unweighted)?** → BFS
- **Shortest path (weighted)?** → Dijkstra
- **Connectivity/components?** → Union-Find or DFS
- **Ordering/dependencies?** → Topological Sort
- **All paths/explore all?** → DFS/Backtracking

## 📐 Templates

### BFS (Shortest path unweighted / Level-order)
```python
from collections import deque
def bfs(graph, start):
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
```

### DFS (Connectivity / Explore all)
```python
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

### Dijkstra (Shortest path weighted)
```python
import heapq
def dijkstra(graph, start):
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float('inf')): continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return dist
```

### Union-Find
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
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
        return True
```

### Topological Sort (Kahn's BFS)
```python
from collections import deque, defaultdict
def topo_sort(num_courses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    queue = deque([i for i in range(num_courses) if indegree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == num_courses else []
```

## 🏋️ Practice Problems (20 problems)

### BFS / DFS Core
| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #200 Number of Islands | Medium | DFS/BFS flood fill |
| 2 | LC #695 Max Area of Island | Medium | DFS tracking area |
| 3 | LC #133 Clone Graph | Medium | BFS/DFS + hash map (old→new) |
| 4 | LC #994 Rotting Oranges | Medium | Multi-source BFS |
| 5 | LC #286 Walls and Gates | Medium | Multi-source BFS from gates |
| 6 | LC #417 Pacific Atlantic Water | Medium | DFS from each ocean inward |

### Shortest Path
| 7 | LC #743 Network Delay Time | Medium | Dijkstra |
| 8 | LC #787 Cheapest Flights K Stops | Medium | Bellman-Ford with K limit |
| 9 | LC #127 Word Ladder | Hard | BFS with wildcard preprocessing |

### Union-Find
| 10 | LC #684 Redundant Connection | Medium | Union-Find: edge that creates cycle |
| 11 | LC #323 Connected Components | Medium | Union-Find or DFS |
| 12 | LC #721 Accounts Merge | Medium | Union-Find + sort |

### Topological Sort
| 13 | LC #207 Course Schedule | Medium | Topo sort: can finish? |
| 14 | LC #210 Course Schedule II | Medium | Topo sort: return order |
| 15 | LC #269 Alien Dictionary | Hard | Build graph from word order + topo sort |

### Advanced
| 16 | LC #130 Surrounded Regions | Medium | DFS from border Os |
| 17 | LC #785 Is Graph Bipartite | Medium | BFS/DFS 2-coloring |
| 18 | LC #1584 Min Cost Connect Points | Medium | Kruskal's MST |
| 19 | LC #332 Reconstruct Itinerary | Hard | DFS + sort + Eulerian path |
| 20 | LC #778 Swim in Rising Water | Hard | Binary search + BFS (or Dijkstra) |
