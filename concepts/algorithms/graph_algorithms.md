# Graph Algorithms

## 1. Traversal: BFS vs. DFS

### BFS (Breadth-First Search)
**Conceptual Overview**: Explore the graph layer by layer. Like a ripple in a pond.
**Data Structure**: **Queue**.
**Best For**: Finding the **shortest path** in an unweighted graph.

### DFS (Depth-First Search)
**Conceptual Overview**: Go as deep as possible down one path before backtracking. Like exploring a maze.
**Data Structure**: **Stack** (or Recursion).
**Best For**: Pathfinding, Cycle detection, Topological sort.

---

## 2. Shortest Path Algorithms

### Dijkstra's Algorithm
**Conceptual Overview**: Finds the shortest path from a starting node to all other nodes in a **weighted graph** (with non-negative weights).
- **Strategy**: Greedy. Always pick the unvisited node with the smallest known distance.
- **Data Structure**: **Min-Heap (Priority Queue)**.
- **Complexity**: O((V + E) log V).

### Bellman-Ford
**Conceptual Overview**: Similar to Dijkstra but can handle **negative weights**.
- **Strategy**: Dynamic Programming. Relax all edges $V-1$ times.
- **Complexity**: O(V * E).
- **Special Power**: Can detect **negative cycles**.

---

## 3. Minimum Spanning Tree (MST)

### Kruskal's Algorithm
**Conceptual Overview**: Connect all nodes with the minimum total edge weight without forming cycles.
- **Strategy**: Greedy. Sort all edges and add them if they don't form a cycle.
- **Data Structure**: **DSU (Union-Find)**.
- **Complexity**: O(E log E).

### Prim's Algorithm
**Conceptual Overview**: Grow the MST from a single starting node.
- **Strategy**: Greedy. Always pick the smallest edge connecting a node in the MST to a node outside it.
- **Data Structure**: **Min-Heap**.
- **Complexity**: O(E log V).

---

## 4. Visual Comparison of BFS vs DFS

```mermaid
graph TD
    subgraph BFS (Layer by Layer)
    B1((1)) --> B2((2))
    B1 --> B3((2))
    B2 --> B4((3))
    B3 --> B5((3))
    end
    
    subgraph DFS (Deep First)
    D1((1)) --> D2((2))
    D2 --> D3((3))
    D3 --> D4((4))
    D1 -.-> D5((Backtrack))
    end
```

---

## 5. Developer Tips & Practical Knowledge

### The "Matrix" BFS Pattern
In grid-based problems (like "Number of Islands"), treat each cell as a node and its neighbors (Up, Down, Left, Right) as edges. A `visited` set is crucial to avoid infinite loops.

### Topological Sort (Kahn's Algorithm)
Used for scheduling tasks with dependencies (e.g., "Course Schedule"). It only works on **Directed Acyclic Graphs (DAGs)**.

### Dijkstra vs. A*
In game dev or GPS apps, **A*** is used instead of Dijkstra. It adds a "heuristic" (estimate of distance to target) to guide the search, making it much faster by exploring only the "correct" direction.
