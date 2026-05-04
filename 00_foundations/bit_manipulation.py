"""
⚡ Bit Manipulation — Easy Points When You Know It
===================================================
Appears in ~5-10% of interviews. Small investment, guaranteed returns.
"""

# ============================================================
# CORE OPERATORS
# ============================================================
"""
& (AND)   — Both bits 1 → 1        | 1010 & 1100 = 1000
| (OR)    — Either bit 1 → 1       | 1010 | 1100 = 1110
^ (XOR)   — Bits differ → 1        | 1010 ^ 1100 = 0110
~ (NOT)   — Flip all bits           | ~1010 = ...0101
<< (LSH)  — Shift left (×2)        | 0001 << 3 = 1000
>> (RSH)  — Shift right (÷2)       | 1000 >> 2 = 0010

KEY XOR PROPERTIES:
  a ^ a = 0       (self-cancel)
  a ^ 0 = a       (identity)
  a ^ b ^ a = b   (find the odd one out)
"""

# ============================================================
# ESSENTIAL TRICKS
# ============================================================

def is_power_of_2(n: int) -> bool:
    """Power of 2 has exactly one bit set: 1000...0
    n & (n-1) clears the lowest set bit.
    If result is 0, only one bit was set."""
    return n > 0 and (n & (n - 1)) == 0

def count_set_bits(n: int) -> int:
    """Count number of 1-bits (Hamming weight). Brian Kernighan's trick."""
    count = 0
    while n:
        n &= (n - 1)  # Clears lowest set bit each iteration
        count += 1
    return count

def get_bit(n: int, i: int) -> int:
    """Get the i-th bit (0-indexed from right)."""
    return (n >> i) & 1

def set_bit(n: int, i: int) -> int:
    """Set the i-th bit to 1."""
    return n | (1 << i)

def clear_bit(n: int, i: int) -> int:
    """Clear the i-th bit (set to 0)."""
    return n & ~(1 << i)

def toggle_bit(n: int, i: int) -> int:
    """Toggle the i-th bit."""
    return n ^ (1 << i)

def single_number(nums: list) -> int:
    """Every element appears twice except one. Find it.
    XOR all numbers: pairs cancel out, single number remains.
    LC #136 — O(N) time, O(1) space."""
    result = 0
    for num in nums:
        result ^= num
    return result

def is_odd(n: int) -> bool:
    """Last bit determines odd/even."""
    return (n & 1) == 1

def swap_without_temp(a: int, b: int) -> tuple:
    """XOR swap (interview trick, not practical)."""
    a ^= b
    b ^= a
    a ^= b
    return a, b

# ============================================================
# BITMASK FOR SUBSETS (Foundation for Bitmask DP)
# ============================================================

def generate_subsets_bitmask(nums: list) -> list:
    """Generate all subsets using bitmask.
    For N elements, iterate 0 to 2^N - 1.
    Each bit position = include/exclude decision.
    
    Example: nums = [a, b, c]
    mask=000 → []     mask=001 → [a]
    mask=010 → [b]    mask=011 → [a,b]
    mask=100 → [c]    mask=101 → [a,c]
    mask=110 → [b,c]  mask=111 → [a,b,c]
    """
    n = len(nums)
    result = []
    for mask in range(1 << n):  # 0 to 2^n - 1
        subset = []
        for i in range(n):
            if mask & (1 << i):  # Check if i-th bit is set
                subset.append(nums[i])
        result.append(subset)
    return result

# ============================================================
# INTERVIEW PROBLEMS
# ============================================================
"""
EASY:
  LC #136 Single Number — XOR all elements
  LC #191 Number of 1 Bits — Brian Kernighan's
  LC #231 Power of Two — n & (n-1) == 0
  LC #190 Reverse Bits — Shift and build

MEDIUM:
  LC #137 Single Number II — Bit counting mod 3
  LC #260 Single Number III — XOR then split by bit
  LC #338 Counting Bits — DP with bit trick

USED IN OTHER PATTERNS:
  Bitmask DP — dp[mask] for subset states (N ≤ 20)
"""


if __name__ == "__main__":
    assert is_power_of_2(16) == True
    assert is_power_of_2(15) == False
    assert count_set_bits(0b1011) == 3
    assert get_bit(0b1010, 1) == 1
    assert get_bit(0b1010, 0) == 0
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert len(generate_subsets_bitmask([1, 2, 3])) == 8
    print("✅ All bit manipulation tests passed!")
