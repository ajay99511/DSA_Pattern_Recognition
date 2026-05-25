# Sorting & Searching: The Efficiency Core

## 1. Binary Search: The "Range Reduction" Schematic
Binary Search isn't just for finding a value; it's for **Search Space Reduction**.

### Schematic: The `[Left, Right]` Collapse
```mermaid
graph LR
    subgraph Iteration_1 [Range: 0-100]
    direction LR
    L1[0] --- M1{50} --- R1[100]
    end
    
    subgraph Iteration_2 [Target > 50]
    direction LR
    L2[51] --- M2{75} --- R2[100]
    end
    
    Iteration_1 -- "low = mid + 1" --> Iteration_2
    style M1 fill:#f9f
    style M2 fill:#6f9
```

**Developer Tip**: Use `low + (high - low) // 2` to avoid integer overflow in languages like C++/Java.

---

## 2. QuickSort: The Partitioning Logic

### Conceptual Overview
The heart of QuickSort is the **Partition** step. We pick a pivot and move everything smaller to the left and larger to the right.

### Schematic: Lomuto Partitioning
```mermaid
graph TD
    subgraph State_1 [Array with Pivot: 5]
    A1[2] --- A2[8] --- A3[3] --- A4[9] --- A5[1] --- A6[Pivot: 5]
    end
    
    subgraph State_2 [Processing 1]
    B1[2] --- B2[3] --- B3[1] --- B4[9] --- B5[8] --- B6[Pivot: 5]
    end
    
    subgraph State_3 [Final Swap]
    C1[2] --- C2[3] --- C3[1] --- C4[Pivot: 5] --- C5[8] --- C6[9]
    end
    
    State_1 --> State_2 --> State_3
    style C4 fill:#6f9
```

---

## 3. Stability & In-Place Algorithms

### A. Sorting Stability
A sort is **Stable** if it preserves the relative order of elements with equal keys.
- **Stable**: Merge Sort, Insertion Sort, Bubble Sort.
- **Unstable**: QuickSort, Heap Sort, Selection Sort.

### B. In-Place Algorithms
An algorithm is **In-Place** if it uses only $O(1)$ extra space (excluding the recursion stack).
- **In-Place**: QuickSort, Heap Sort, Insertion Sort.
- **Not In-Place**: Merge Sort (requires $O(n)$ extra space).

---

## 4. Advanced Sub-Topics

### Counting Sort & Radix Sort
Non-comparison based sorting that can achieve **O(n)** time.
- **Requirement**: The data must be integers within a specific range.

### Search Space Binary Search
Applying binary search on the **Answer** instead of the input array.
- **Example**: "Minimum time to complete all tasks" where you binary search between `min_time` and `max_time`.

---

## 5. Developer Cheat Sheet

| Algorithm | Average Time | Space | Stable? | When to use? |
| :--- | :--- | :--- | :--- | :--- |
| **QuickSort** | $O(n \log n)$ | $O(\log n)$ | No | General purpose, fast in-place |
| **MergeSort** | $O(n \log n)$ | $O(n)$ | **Yes** | Linked lists, Stability needed |
| **HeapSort** | $O(n \log n)$ | **O(1)** | No | Limited memory |
| **Timsort** | $O(n \log n)$ | $O(n)$ | **Yes** | Most real-world data (Hybrid) |

### Critical Patterns
- **Median of Three**: Improving QuickSort pivot selection.
- **Kth Largest Element**: Using QuickSelect (average $O(n)$).
- **Binary Search on Answer**: Solving optimization problems.
