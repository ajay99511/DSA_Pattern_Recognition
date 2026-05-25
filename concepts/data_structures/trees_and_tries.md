# Trees & Tries: Hierarchical Architecture

## 1. Binary Search Trees (BST) & Balancing

### Schematic: AVL Rotations (Restoring Balance)
A BST becomes inefficient ($O(n)$) if it becomes skewed. **AVL Trees** use rotations to maintain $O(\log n)$ height.

```mermaid
graph TD
    subgraph Right_Rotation [Left-Left Case]
    direction TB
    C((C)) --> B((B))
    B --> A((A))
    
    B_Rotate[Rotate B Right]
    
    B1((B)) --> A1((A))
    B1 --> C1((C))
    end
    
    C -.-> B_Rotate -.-> B1
    
    style B1 fill:#6f9
```

---

## 2. Heaps: The Array-Based Tree

### Conceptual Overview
Heaps are **Complete Binary Trees** stored in an **Array**.
- Parent of $i$: `(i-1) // 2`
- Children of $i$: `2i + 1`, `2i + 2`

### Schematic: Heapify (Sift-Up / Sift-Down)
When inserting into a **Max-Heap**, we add to the end and "Sift-Up".

```mermaid
graph TD
    subgraph Sift_Up [Insert 50 into Max-Heap]
    Root((40)) --> L((30))
    Root --> R((20))
    L --> LL((10))
    L --> New((50))
    
    Swap[Swap 50 with 30, then with 40]
    
    Final_Root((50)) --> Final_L((40))
    Final_Root --> Final_R((20))
    Final_L --> F_LL((10))
    Final_L --> F_New((30))
    end
    
    New -.-> Swap -.-> Final_Root
    
    style New fill:#f9f
    style Final_Root fill:#6f9
```

---

## 3. Tries: The Prefix Schematic

### Schematic: Storing "CAT" and "CAR"
```mermaid
graph TD
    Root(( )) --> C((c))
    C --> A((a))
    A --> T((t*))
    A --> R((r*))
    
    style T fill:#dfd
    style R fill:#dfd
```
**Space Efficiency**: Common prefixes are shared, making Tries ideal for dictionary lookups.

---

## 4. Tree Traversals: The Three Perspectives

### A. Depth-First Search (DFS)
- **In-Order (L-Root-R)**: Sorted order for BSTs.
- **Pre-Order (Root-L-R)**: Good for cloning trees.
- **Post-Order (L-R-Root)**: Bottom-up processing (e.g., subtree size).

### B. Breadth-First Search (BFS / Level-Order)
Visits nodes layer by layer using a **Queue**.

### C. Iterative vs. Recursive
- **Recursive**: Simple to write, uses the **Stack** (can lead to StackOverflow for deep trees).
- **Iterative**: Uses an explicit **Stack** or **Queue**, safer for massive trees.

---

## 5. Developer Cheat Sheet

| Tree Type | Key Property | Use Case |
| :--- | :--- | :--- |
| **BST** | Sorted order | General searching |
| **Heap** | Min/Max at root | Priority Queues, Top-K problems |
| **AVL / Red-Black** | Self-balancing | `std::map` (C++), `TreeMap` (Java) |
| **Segment Tree** | Range queries | Sum/Min in a range |
| **Trie** | Prefix sharing | Autocomplete, IP routing |

### Critical Patterns
- **LCA (Lowest Common Ancestor)**: Find the first common parent.
- **Path Sum**: Tracking state down a branch.
- **Diameter of Tree**: Longest path between any two nodes.
