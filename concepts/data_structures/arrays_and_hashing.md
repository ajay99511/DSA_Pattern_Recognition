# Arrays & Hashing: Architectural Deep Dive

## 1. The Physical Layer: Memory Layout

### Schematic: Contiguous Memory vs. Sparse Access
An array is a promise of **Cache Locality**. The CPU doesn't just fetch one element; it fetches a "Cache Line" containing neighbors.

```mermaid
graph LR
    subgraph RAM [Physical RAM Layout]
    direction LR
    M1[0x00: Val 10] --- M2[0x04: Val 20] --- M3[0x08: Val 30] --- M4[0x0C: Val 40]
    M4 --- M5[0x10: Empty] --- M6[0x14: Empty]
    end
    
    subgraph CPU_Cache [L1/L2 Cache Line]
    C1[Val 10] --- C2[Val 20] --- C3[Val 30] --- C4[Val 40]
    end
    
    RAM -- "Prefetch Line" --> CPU_Cache
    
    style M1 fill:#f9f,stroke:#333
    style M2 fill:#f9f,stroke:#333
    style M3 fill:#f9f,stroke:#333
    style M4 fill:#f9f,stroke:#333
    style CPU_Cache fill:#dfd,stroke:#090,stroke-dasharray: 5 5
```

---

## 2. Dynamic Arrays: The Resizing Mechanic

### Conceptual Overview
When a dynamic array (like `std::vector` or Python `list`) exceeds its **Capacity**, it performs an "Amortized" operation:
1. Allocates a new block of memory (usually **2x** the size).
2. Copies all elements to the new block.
3. Frees the old block.

### Schematic: The Double-and-Copy Strategy
```mermaid
graph TD
    subgraph Step1 [1. Capacity Full]
    A1[1] --- A2[2] --- A3[3] --- A4[4]
    end
    
    subgraph Step2 [2. Allocate & Copy]
    B1[1] --- B2[2] --- B3[3] --- B4[4] --- B5[ ] --- B6[ ] --- B7[ ] --- B8[ ]
    A1 -.-> B1
    A2 -.-> B2
    A3 -.-> B3
    A4 -.-> B4
    end
    
    subgraph Step3 [3. Final State]
    C1[1] --- C2[2] --- C3[3] --- C4[4] --- C5[NEW] --- C6[ ] --- C7[ ] --- C8[ ]
    end
    
    style A1 fill:#f66
    style A4 fill:#f66
    style C5 fill:#6f9
```

---

## 3. Hash Tables: The Collision Battlefield

### Schematic: Collision Resolution (Chaining vs Open Addressing)

#### A. Separate Chaining (Linked Lists)
```mermaid
graph LR
    subgraph Buckets
    B0[Index 0]
    B1[Index 1]
    B2[Index 2]
    end
    
    B0 --> N1[Key: 'Alice'] --> N2[Key: 'Zoe']
    B2 --> N3[Key: 'Bob']
    
    style N2 fill:#ffd,stroke:#333
    style B0 fill:#eee
```

#### B. Open Addressing (Linear Probing)
```mermaid
graph LR
    subgraph Array_Slots
    S0[Alice]
    S1[Zoe - Collided & Moved]
    S2[Bob]
    S3[Empty]
    end
    
    HashZoe['Zoe' hashes to 0] -.-> S0
    S0 -- "Slot Taken" --> S1
    
    style S1 fill:#f96,stroke:#333
```

---

## 4. Advanced Sub-Topics & Nuances

### Hash Functions: The "Uniform Distribution" Goal
A high-quality hash function must:
1. **Deterministic**: Same input $\rightarrow$ Same output.
2. **Fast**: O(1) time to compute.
3. **Minimize Collisions**: Spread keys across the entire table.

### Load Factor ($\alpha$)
$\alpha = \frac{n}{k}$ where $n$ is the number of entries and $k$ is the number of buckets.
- **Threshold**: Usually 0.7 to 0.75.
- **When $\alpha > Threshold$**: Performance drops from $O(1)$ toward $O(n)$. The table **must** resize (rehash).

---

## 5. Developer Cheat Sheet

| Feature | Static Array | Dynamic Array | Hash Map |
| :--- | :--- | :--- | :--- |
| **Search (Key)** | O(n) | O(n) | **O(1) Avg** / O(n) Worst |
| **Access (Index)** | **O(1)** | **O(1)** | N/A |
| **Insert (End)** | O(1) / N/A | **O(1) Amortized** | **O(1) Avg** |
| **Memory** | Fixed | Dynamic (Over-allocated) | Large Overhead |

### Critical Patterns
- **Prefix Sums**: Range queries in $O(1)$.
- **Two Pointers**: Collapsing search space.
- **Sliding Window**: Dynamic range processing.
- **Difference Array**: Batch updates to ranges.
