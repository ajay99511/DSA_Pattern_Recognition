# Stacks & Queues: Strategic Data Structures

## 1. Stack: The LIFO Powerhouse

### Schematic: The Function Call Stack
Modern programming depends on the stack for recursion and function calls.

```mermaid
graph BT
    subgraph RAM_Stack [Memory Stack Frame]
    direction BT
    F1[main()] --- F2[getUser()] --- F3[dbQuery()]
    end
    
    subgraph CPU_Ops [Stack Operations]
    Push((Push)) -.-> F3
    F3 -.-> Pop((Pop))
    end
    
    style F3 fill:#f96,stroke:#333
    style RAM_Stack fill:#f0f0f0
```

---

## 2. Queue: The FIFO Pipeline

### Schematic: Circular Queue (Optimized Memory)
In a static array, a standard queue eventually runs out of space at the back even if the front is empty. A **Circular Queue** wraps around.

```mermaid
graph TD
    subgraph Circular_Memory [The Modulo Loop]
    direction TB
    S0[Data 0] --- S1[Data 1] --- S2[Data 2] --- S3[Head] --- S4[Data 4] --- S5[Tail] --- S6[Empty] --- S7[Empty]
    S7 --- S0
    end
    
    Head_Ptr[Head Index] -.-> S3
    Tail_Ptr[Tail Index] -.-> S5
    
    style S3 fill:#6f9
    style S5 fill:#f66
```
**Formula**: `(index + 1) % capacity`

---

## 3. The Interview Killer: Monotonic Stack

### Conceptual Overview
A stack where elements are kept in a specific order (always increasing or always decreasing). When a new element breaks the order, we "pop" until the order is restored.

### Schematic: Next Greater Element
Problem: Find the first element to the right that is larger than the current.

```mermaid
graph LR
    subgraph Input_Array
    direction LR
    A1[2] --- A2[1] --- A3[5] --- A4[3]
    end
    
    subgraph Stack_State [Monotonic Decreasing Stack]
    S1[Index 1: Val 1]
    S2[Index 0: Val 2]
    end
    
    NewVal[Val 5 arrives] -- "5 > 1 & 5 > 2" --> PopAll[Pop 1 and 2]
    PopAll -- "Mark Answer" --> Result[Result for 1 & 2 is 5]
    
    style S1 fill:#f9f
    style NewVal fill:#6f9
```

**Complexity**: $O(n)$ total (each element is pushed and popped exactly once).

---

## 4. Advanced Sub-Topics

### Deque (Double-Ended Queue)
Implemented typically as a **Doubly Linked List** or a **Circular Dynamic Array**.
- **Use Case**: Sliding Window Maximum problem ($O(n)$ solution).

### Priority Queue vs. Standard Queue
A Priority Queue is NOT a queue in the traditional sense; it's a **Heap**. Use it when you need to "process the most important item first" rather than "first come, first served".

---

## 5. Developer Cheat Sheet

| Data Structure | Best Implementation | Primary Use Case |
| :--- | :--- | :--- |
| **Stack** | Dynamic Array (`ArrayList`) | DFS, Undo, Expression Parsing |
| **Queue** | Linked List (`LinkedList`) | BFS, Task Scheduling |
| **Deque** | `ArrayDeque` (Java) / `collections.deque` (Py) | Sliding Windows |

### Critical Patterns
- **Monotonic Stack**: For range-based comparisons (Next Greater/Smaller).
- **Two Stacks = Queue**: Classic design problem.
- **BFS with Queue**: Layer-by-layer traversal.
