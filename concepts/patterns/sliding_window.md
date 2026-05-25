# Algorithmic Pattern: Sliding Window

## 1. Conceptual Overview
The **Sliding Window** pattern is used to perform a required operation on a specific window size of a given array or linked list, such as finding the longest subarray containing all ones.

**Analogy**: A camera lens moving across a long panorama. You only see a "window" of the scene at any time.

---

## 2. Fixed vs. Dynamic Window

### A. Fixed Window
The window size $K$ is constant.
- **Goal**: Find max sum of $K$ elements.
- **Logic**: Add new element, remove oldest element.

### Schematic: Fixed Window (K=3)
```mermaid
graph LR
    subgraph W1 [Window 1]
    direction LR
    A1[2] --- A2[1] --- A3[5]
    end
    A4[1] --- A5[3]
    
    W1 -- "Slide" --> W2
    
    subgraph W2 [Window 2]
    direction LR
    B1[1] --- B2[5] --- B3[1]
    end
    
    style W2 fill:#dfd
```

### B. Dynamic Window
The window size grows or shrinks based on a condition.
- **Goal**: Longest substring with no repeating characters.
- **Logic**: Expand `right` pointer until condition fails, then shrink `left` pointer.

---

## 3. The Deque Optimization (Sliding Window Maximum)

### Conceptual Overview
Finding the maximum in every sliding window of size $K$ in $O(n)$ time.

### Schematic: Monotonic Deque
```mermaid
graph LR
    subgraph Deque [Monotonic Decreasing]
    direction LR
    D1[Val: 10] --- D2[Val: 7] --- D3[Val: 2]
    end
    
    NewVal[Val 12 arrives] -- "12 > 10, 7, 2" --> Clear[Pop all]
    Clear --> Final[Val: 12]
    
    style Final fill:#6f9
```

---

## 4. Developer Cheat Sheet

| Feature | Fixed Window | Dynamic Window |
| :--- | :--- | :--- |
| **Complexity** | $O(n)$ | $O(n)$ |
| **Pointers** | $i, i+k$ | $left, right$ |
| **State** | Sum, Avg | Map/Set of frequencies |

### Critical Patterns
- **Hash Map + Window**: For substring problems with character counts.
- **Shrink Condition**: Always use a `while` loop to shrink the window until the condition is met.
- **Max vs. Min**: Be careful with what you are tracking (e.g., longest vs. shortest).
