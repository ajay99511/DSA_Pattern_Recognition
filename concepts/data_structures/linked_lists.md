# Linked Lists

## 1. Conceptual Overview
A **Linked List** is a linear data structure where elements are not stored at contiguous memory locations. Instead, each element (node) points to the next one using a reference (pointer).

**Analogy**: Think of a scavenger hunt. Each clue you find tells you where the *next* clue is hidden. You don't know where the 5th clue is until you find the first four.

## 2. Visual Representation

### Singly Linked List
```mermaid
graph LR
    subgraph Singly Linked List
    Head[Head] --> Node1[Val: 10 | Next]
    Node1 --> Node2[Val: 20 | Next]
    Node2 --> Node3[Val: 30 | NULL]
    end
    style Head fill:#dfd,stroke:#333
    style Node3 fill:#fdd,stroke:#333
```

### Doubly Linked List
```mermaid
graph LR
    subgraph Doubly Linked List
    Node1[Prev | Val: 10 | Next] <--> Node2[Prev | Val: 20 | Next] <--> Node3[Prev | Val: 30 | Next]
    end
```

## 3. Types of Linked Lists
1. **Singly Linked List**: Each node has `data` and `next`.
2. **Doubly Linked List**: Each node has `data`, `next`, and `prev`. Allows bidirectional traversal.
3. **Circular Linked List**: The last node points back to the first node. Used in round-robin scheduling.

## 4. Key Properties & Complexity
- **Dynamic Size**: Can grow or shrink at runtime without reallocating the entire structure.
- **No Random Access**: To get to the $n$-th element, you must traverse $n-1$ nodes.
- **Memory Overhead**: Extra memory is required for pointers.

| Operation | Time Complexity (Average/Worst) |
| :--- | :--- |
| **Access (at Index)** | O(n) |
| **Search (for Value)** | O(n) |
| **Insertion (at Head)** | O(1) |
| **Insertion (at Tail)** | O(1)* (with tail pointer) |
| **Deletion (at Head)** | O(1) |

## 5. Developer Tips & Implementation Nuances

### Sentinel Nodes (The "Dummy" Node)
One of the best techniques for linked list problems is using a **Sentinel (Dummy) Node**. It simplifies edge cases (like inserting at the head or deleting the only node) by ensuring there is always a "previous" node to work with.

### Space Complexity vs. Arrays
While Linked Lists are dynamic, they are often *less* efficient than arrays for small datasets due to:
1. **Pointer Overhead**: On a 64-bit system, a pointer is 8 bytes. If your data is a 4-byte integer, you're using 12 bytes per node (3x overhead).
2. **Cache Misses**: Nodes are scattered in memory, so the CPU cannot pre-fetch them into the cache.

### When to use?
- When you need frequent insertions/deletions at the beginning or end.
- When you don't know the size of the data in advance and want to avoid the $O(n)$ cost of array resizing.
- Implementing stacks, queues, or graphs (adjacency lists).
