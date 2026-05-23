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

def missing_number(nums: list) -> int:
    """Find missing number in [0..n] using XOR.
    XOR all indices 0..n with all values: pairs cancel, missing remains.
    LC #268 — O(N) time, O(1) space."""
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result

def hamming_distance(x: int, y: int) -> int:
    """Count positions where bits differ.
    XOR gives 1 where bits differ, then count set bits.
    LC #461 — O(1) time."""
    return count_set_bits(x ^ y)

def reverse_bits(n: int) -> int:
    """Reverse all 32 bits of an unsigned integer.
    Shift result left and pull LSB of n each iteration.
    LC #190 — O(32) = O(1) time."""
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

def single_number_iii(nums: list) -> list:
    """Two elements appear once, rest appear twice. Find both.
    Step 1: XOR all → xor = a ^ b (a and b are the two singles)
    Step 2: Find any set bit in xor (a and b differ here)
    Step 3: Partition nums by that bit → each group XORs to one answer.
    LC #260 — O(N) time, O(1) space."""
    xor = 0
    for num in nums:
        xor ^= num
    # Find rightmost set bit (a and b differ here)
    diff_bit = xor & (-xor)  # isolates lowest set bit
    a = 0
    for num in nums:
        if num & diff_bit:
            a ^= num
    b = xor ^ a
    return [a, b]

def counting_bits(n: int) -> list:
    """Return array where ans[i] = number of 1-bits in i, for 0 <= i <= n.
    DP trick: ans[i] = ans[i >> 1] + (i & 1)
    (right shift removes last bit; add 1 if last bit was set)
    LC #338 — O(N) time, O(N) space."""
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans

def single_number_ii(nums: list) -> int:
    """Every element appears 3 times except one. Find it.
    Count bits mod 3: if a bit appears 3k times it cancels.
    The remaining bits form the single number.
    LC #137 — O(32N) = O(N) time, O(1) space."""
    result = 0
    for bit in range(32):
        bit_sum = sum((num >> bit) & 1 for num in nums)
        if bit_sum % 3:
            result |= (1 << bit)
    # Handle negative numbers (Python uses arbitrary precision ints)
    if result >= (1 << 31):
        result -= (1 << 32)
    return result

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

# ---- Bitmask DP Template (N ≤ 20) ----
"""
BITMASK DP PATTERN:
  State: dp[mask] = best value achievable using the set of items in mask
  Transition: for each mask, try adding item i not yet in mask
              dp[mask | (1 << i)] = combine(dp[mask], cost[i])
  Answer: dp[(1 << n) - 1]  (all items used)
  
  State space: O(2^N * N)  — feasible for N ≤ 20
  
COMMON BITMASK OPERATIONS:
  mask | (1 << i)   → add item i to set
  mask & ~(1 << i)  → remove item i from set
  mask & (1 << i)   → check if item i is in set
  mask ^ (1 << i)   → toggle item i
  (1 << n) - 1      → full set of n items (all bits set)
  mask & (mask - 1) → remove lowest set bit (Brian Kernighan)
  mask & (-mask)    → isolate lowest set bit
  bin(mask).count('1') → popcount (or use count_set_bits above)

ITERATING OVER SUBMASKS of a given mask (useful in DP):
  sub = mask
  while sub > 0:
      # process submask `sub`
      sub = (sub - 1) & mask  # next smaller submask
"""

def bitmask_dp_example(costs: list) -> int:
    """Minimum cost to visit all N cities exactly once (TSP-style).
    dp[mask][i] = min cost to visit cities in `mask`, ending at city i.
    
    This is the classic Traveling Salesman / Assignment skeleton.
    N ≤ 20 for feasibility (2^20 * 20 ≈ 20M states).
    """
    n = len(costs)
    INF = float('inf')
    # dp[mask][i] = min cost to reach state `mask` ending at node i
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # start at node 0, only node 0 visited

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue  # already visited
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + costs[u][v])

    full_mask = (1 << n) - 1
    return min(dp[full_mask][i] for i in range(n))

# ============================================================
# INTERVIEW PROBLEMS
# ============================================================
"""
EASY:
  LC #136 Single Number       — XOR all elements → O(N) time, O(1) space
                                 Signal: "every element appears twice except one"
  LC #191 Number of 1 Bits    — Brian Kernighan's n &= (n-1) loop
                                 Signal: "count set bits / Hamming weight"
  LC #231 Power of Two        — n > 0 and n & (n-1) == 0
                                 Signal: "check if power of 2"
  LC #190 Reverse Bits        — 32-iteration shift-and-build
                                 Signal: "reverse all bits of 32-bit integer"
  LC #268 Missing Number      — XOR indices 0..n with all values
                                 Signal: "find missing in [0..n]" (also Gauss sum)
  LC #461 Hamming Distance    — count_set_bits(x ^ y)
                                 Signal: "positions where bits differ"

MEDIUM:
  LC #137 Single Number II    — Bit counting mod 3 across all 32 positions
                                 Signal: "every element appears 3 times except one"
  LC #260 Single Number III   — XOR all → find diff bit → partition and XOR
                                 Signal: "two elements appear once, rest appear twice"
  LC #338 Counting Bits       — DP: ans[i] = ans[i >> 1] + (i & 1)
                                 Signal: "count 1-bits for all numbers 0..n"
  LC #201 Bitwise AND Range   — Right-shift both until equal, track shifts
                                 Signal: "bitwise AND of all numbers in [left, right]"
  LC #371 Sum of Two Integers — a ^ b (sum without carry) + (a & b) << 1 (carry)
                                 Signal: "add without + operator"

HARD / BITMASK DP:
  LC #847 Shortest Path Visiting All Nodes — BFS + bitmask state (N ≤ 12)
  LC #1986 Minimum Number of Work Sessions — Bitmask DP (N ≤ 14)
  LC #1125 Smallest Sufficient Team        — Bitmask DP on skill sets (N ≤ 26)
  LC #943  Find the Shortest Superstring   — TSP-style Bitmask DP (N ≤ 12)

RECOGNITION SIGNALS — reach for bit tricks when you see:
  • "appears twice except one" → XOR
  • "power of 2" → n & (n-1)
  • "count 1-bits" → Brian Kernighan
  • "subset enumeration" + N ≤ 20 → Bitmask DP
  • "visit all nodes/items" + N ≤ 20 → Bitmask DP (TSP)
  • "add/subtract without arithmetic operators" → XOR + AND shift

USED IN OTHER PATTERNS:
  Bitmask DP  — dp[mask] for subset states (N ≤ 20); see bitmask_dp_example above
  Backtracking — use bitmask instead of visited[] set for O(1) membership check
  Graphs       — bitmask state in BFS for "visit all nodes" problems
  Greedy       — bit tricks for fast modular arithmetic and power-of-2 checks
"""


if __name__ == "__main__":
    # Core tricks
    assert is_power_of_2(16) == True
    assert is_power_of_2(15) == False
    assert count_set_bits(0b1011) == 3
    assert get_bit(0b1010, 1) == 1
    assert get_bit(0b1010, 0) == 0
    assert set_bit(0b1010, 0) == 0b1011
    assert clear_bit(0b1011, 0) == 0b1010
    assert toggle_bit(0b1010, 0) == 0b1011

    # XOR applications
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert swap_without_temp(3, 5) == (5, 3)
    assert missing_number([3, 0, 1]) == 2
    assert hamming_distance(1, 4) == 2   # 001 vs 100 → 2 differing bits
    assert reverse_bits(0b00000010100101000001111010011100) == 0b00111001011110000010100101000000
    assert sorted(single_number_iii([1, 2, 1, 3, 2, 5])) == [3, 5]
    assert counting_bits(5) == [0, 1, 1, 2, 1, 2]
    assert single_number_ii([2, 2, 3, 2]) == 3

    # Bitmask subsets
    assert len(generate_subsets_bitmask([1, 2, 3])) == 8

    print("✅ All bit manipulation tests passed!")
