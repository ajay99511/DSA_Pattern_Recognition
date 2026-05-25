# Advanced Topics: Bit Manipulation & Math

## 1. Bit Manipulation

### Conceptual Overview
Everything in a computer is stored in bits (0s and 1s). Bit manipulation involves using bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`) to perform calculations at the lowest level. It is incredibly fast and memory-efficient.

### The "Magic" Operators
- **AND (`&`)**: `1 & 1 = 1`, otherwise `0`. Used to check if a bit is set.
- **OR (`|`)**: `0 | 0 = 0`, otherwise `1`. Used to set a bit.
- **XOR (`^`)**: `1 ^ 1 = 0`, `0 ^ 0 = 0`, `1 ^ 0 = 1`. **Property**: `x ^ x = 0` and `x ^ 0 = x`.
- **NOT (`~`)**: Flips all bits.
- **Shifts (`<<`, `>>`)**: Moves bits left or right. `x << 1` is effectively $x \times 2$.

### Common Tricks for Developers
1. **Check if Even/Odd**: `(n & 1) == 0` is even.
2. **Power of Two**: `(n & (n - 1)) == 0` checks if $n$ is a power of 2.
3. **Swap numbers**: `a^=b; b^=a; a^=b;` swaps without a temporary variable.
4. **Find the unique number**: In an array where every number appears twice except one, XORing all elements results in the unique number.

---

## 2. Essential Math for DSA

### Prime Numbers
- **Sieve of Eratosthenes**: Finds all primes up to $N$ in $O(N \log \log N)$.

### Greatest Common Divisor (GCD)
- **Euclidean Algorithm**:
  ```python
  def gcd(a, b):
      while b:
          a, b = b, a % b
      return a
  ```

### Modular Arithmetic
When dealing with large numbers, you often need to return `result % (10^9 + 7)`.
- **Addition**: `(a + b) % m = ((a % m) + (b % m)) % m`
- **Multiplication**: `(a * b) % m = ((a % m) * (b % m)) % m`
- **Division**: Requires **Modular Multiplicative Inverse** (via Fermat's Little Theorem).

---

## 3. Geometry Basics

### Distance Formula
$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$

### Cross Product
Used to determine if three points form a clockwise or counter-clockwise turn (crucial for Convex Hull algorithms).

### Overlapping Rectangles
Two rectangles $[x1, y1, x2, y2]$ and $[x3, y3, x4, y4]$ overlap if:
- `max(x1, x3) < min(x2, x4)` AND `max(y1, y3) < min(y2, y4)`.

---

## 4. Visual Representation: Bitmasking
Imagine a set of 5 options. You can represent which ones are selected using a single integer (0-31).

```mermaid
graph LR
    subgraph Bitmask: 13 (1101)
    B3[Bit 3: ON]
    B2[Bit 2: ON]
    B1[Bit 1: OFF]
    B0[Bit 0: ON]
    end
    style B3 fill:#6f9
    style B2 fill:#6f9
    style B1 fill:#f66
    style B0 fill:#6f9
```
