# Two Pointers

> **Module 02 of 16** | Phase 2: Linear Patterns | Week 3
>
> Master the art of eliminating nested loops — reduce O(N²) brute force to O(N) by exploiting sorted order or in-place invariants with two coordinated indices.

---

## 🎯 When to Use This Pattern

**Signal words** (any of these in the problem → think Two Pointers first):
- `"sorted array"` / `"sorted input"` → opposite-direction pair finding
- `"pair with sum"` / `"two numbers summing to target"` → opposite-direction on sorted array
- `"remove duplicates"` / `"remove element in-place"` → same-direction slow/fast
- `"move zeroes"` / `"partition array"` → same-direction slow/fast
- `"palindrome"` / `"reverse"` → opposite-direction character comparison
- `"container with water"` / `"maximize area"` → opposite-direction, move shorter side
- `"trapping rain water"` → opposite-direction tracking running max
- `"3Sum"` / `"triplet"` / `"quadruplet"` → fix one element + opposite-direction on remainder
- `"sort colors"` / `"Dutch National Flag"` → three-pointer partition

**Input characteristics that suggest this pattern**:
- Array is **sorted** (or can be sorted without losing information)
- Problem requires **O(1) extra space** — no auxiliary data structures allowed
- Need to find **pairs or triplets** satisfying a sum/difference condition
- Need to **partition or rearrange** elements in-place
- Brute force is O(N²) — two pointers typically reduces it to O(N) or O(N log N)
- Comparing or combining elements from **opposite ends** of the array

**When NOT to use**:
- Array is **unsorted** and sorting would lose information → prefer Hash Map (O(N) time, O(N) space)
- Need to find a **single element** satisfying a condition → prefer Binary Search
- Need a **contiguous subarray** with a running constraint → prefer Sliding Window
- Need to track **cycle detection** in a linked list → prefer Fast & Slow Pointers (Floyd's)

---

## 🧠 Core Concept

### Why Two Pointers beats O(N²) brute force

The brute-force approach to "find a pair in a sorted array summing to target" checks every pair:

```
for i in range(n):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target: ...   # O(N²) — too slow
```

Two pointers exploits the **sorted order** to make a binary decision at each step:
- If `nums[left] + nums[right] < target` → the sum is too small; only increasing `left` can help
- If `nums[left] + nums[right] > target` → the sum is too large; only decreasing `right` can help
- Each step eliminates one element from consideration, so the total work is O(N)

```
left, right = 0, n-1
while left < right:
    s = nums[left] + nums[right]
    if s == target: found!
    elif s < target: left += 1    # Eliminate nums[left] — no pair with it sums to target
    else: right -= 1              # Eliminate nums[right] — no pair with it sums to target
```

**The key insight**: sorted order gives you a **monotonic relationship** between pointer positions and the sum. Moving a pointer in one direction always increases (or always decreases) the sum, so you can make a greedy decision at every step.

### Opposite-direction: converge from both ends

Start `left = 0`, `right = n-1`. Both pointers move **inward** toward each other. The loop terminates when they meet (`left >= right`). This pattern works when:
- The array is sorted and you're searching for a pair
- You're comparing characters from both ends (palindrome)
- You're maximizing/minimizing a value that depends on both endpoints (container water)

```
[2, 7, 11, 15]   target = 9
 L           R   → sum = 17 > 9 → move R left
 L       R       → sum = 13 > 9 → move R left
 L   R           → sum = 9 == target ✓
```

### Same-direction: slow/fast pointers

Both pointers start at the beginning. `fast` always advances; `slow` only advances when a condition is met. This creates a **write pointer** (`slow`) and a **read pointer** (`fast`). Use when:
- Removing elements in-place (slow = next write position)
- Deduplicating a sorted array (slow = last unique element)
- Partitioning elements (slow = boundary between two groups)

```
[0, 1, 0, 3, 12]   Move Zeroes
 S  F              → nums[F] != 0 → swap, slow++
    S     F        → nums[F] == 0 → fast++ only
    S        F     → nums[F] != 0 → swap, slow++
       S        F  → done
Result: [1, 3, 12, 0, 0]
```

### When sorted order enables the technique

Two pointers on unsorted arrays only works for same-direction patterns (slow/fast for partitioning). For opposite-direction pair finding, **sorted order is mandatory** — it's what gives you the monotonic property that lets you eliminate elements with certainty.

If the array is unsorted and you need pair finding, you have two choices:
1. Sort first → O(N log N) time, O(1) extra space → use two pointers
2. Use a hash map → O(N) time, O(N) extra space → use complement lookup

For FAANG interviews, if the problem says "sorted input", two pointers is almost always the intended O(N) solution.

---

## 📐 Template Code (Python)

### Template 1: Opposite Direction (Two Sum II style)

Use when: sorted array, find pair/triplet satisfying a sum condition, palindrome check, maximize/minimize value at two endpoints.

```python
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1    # Start from both ends of the sorted array

    while left < right:               # Loop until pointers meet — each iteration eliminates one element
        curr_sum = nums[left] + nums[right]

        if curr_sum == target:
            return [left + 1, right + 1]  # Problem uses 1-indexed output (LC #167)

        elif curr_sum < target:
            left += 1                 # Sum too small → need a larger left value
                                      # Safe because: any pair with nums[left] sums to < target
                                      # (right is already the largest possible partner)

        else:
            right -= 1                # Sum too large → need a smaller right value
                                      # Safe because: any pair with nums[right] sums to > target
                                      # (left is already the smallest possible partner)

    return []                         # No valid pair found


# --- Palindrome variant (opposite-direction character comparison) ---
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from both ends
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False              # Mismatch found — not a palindrome

        left += 1                     # Characters matched — move both inward
        right -= 1

    return True                       # All characters matched


# --- Container With Most Water variant (maximize area) ---
def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        # Area = width × min height (the shorter wall is the bottleneck)
        width = right - left
        water = min(height[left], height[right]) * width
        max_water = max(max_water, water)

        # Key insight: moving the TALLER pointer inward can only decrease area
        # (width shrinks AND height is bounded by the shorter wall anyway)
        # Moving the SHORTER pointer inward might find a taller wall → only hope for improvement
        if height[left] < height[right]:
            left += 1                 # Left is shorter — move it inward
        else:
            right -= 1                # Right is shorter (or equal) — move it inward

    return max_water
```

**Key decisions to customize**:
- Change the condition `curr_sum == target` to match your problem (difference, product, etc.)
- For palindrome: adjust the `isalnum()` filter based on what characters to skip
- For maximize/minimize: identify which pointer to move (always move the one that's the bottleneck)
- Return indices vs. values depending on what the problem asks

**Complexity**: Time O(N), Space O(1)

---

### Template 2: Same Direction (Remove Duplicates / Partition style)

Use when: in-place removal, deduplication of sorted array, partitioning elements, moving elements to one end.

```python
def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    slow = 0                          # slow = index of the last confirmed unique element
                                      # Everything at indices [0..slow] is the "clean" prefix

    for fast in range(1, len(nums)):  # fast scans every element exactly once
        if nums[fast] != nums[slow]:  # Found a new unique element
            slow += 1                 # Advance slow to the next write position
            nums[slow] = nums[fast]   # Write the new unique element into the clean prefix

    return slow + 1                   # Length of deduplicated array (slow is 0-indexed)


# --- Move Zeroes variant (partition: non-zeros first, zeros last) ---
def move_zeroes(nums: list[int]) -> None:
    slow = 0                          # slow = next position to place a non-zero element

    for fast in range(len(nums)):
        if nums[fast] != 0:           # Found a non-zero element
            nums[slow], nums[fast] = nums[fast], nums[slow]  # Swap into position
            slow += 1                 # Advance the write pointer
                                      # NOTE: swap (not just assign) preserves zeros at the back


# --- Squares of Sorted Array variant (merge from outside in) ---
def sorted_squares(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1                       # Fill result from the back (largest squares first)

    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2

        if left_sq > right_sq:        # Left square is larger — place it at current back position
            result[pos] = left_sq
            left += 1
        else:                         # Right square is larger (or equal)
            result[pos] = right_sq
            right -= 1

        pos -= 1                      # Move back position leftward

    return result
```

**Key decisions to customize**:
- Change the condition `nums[fast] != nums[slow]` to match your "keep" criterion
- Use swap vs. assign: swap when you need to preserve the displaced elements (Move Zeroes); assign when you don't care (Remove Duplicates)
- For "allow at most K duplicates": change condition to `fast - slow >= k` or track a count
- For Squares: fill from back because the largest squares come from the extremes of a sorted array

**Complexity**: Time O(N), Space O(1) for in-place; O(N) for Squares (output array)

---

### Template 3: Partition (Dutch National Flag / 3-way partition)

Use when: Sort Colors (0/1/2), partition around a pivot, 3-way partition for any 3-valued array.

```python
def sort_colors(nums: list[int]) -> None:
    """
    Dutch National Flag algorithm — partition into three groups in one pass.
    Invariant at all times:
      nums[0..low-1]   = all 0s  (red)
      nums[low..mid-1] = all 1s  (white)
      nums[mid..high]  = unknown (unprocessed)
      nums[high+1..n-1]= all 2s  (blue)
    """
    low = 0                           # Boundary: everything before low is 0
    mid = 0                           # Current element being examined
    high = len(nums) - 1              # Boundary: everything after high is 2

    while mid <= high:                # Process until mid crosses high (unknown region exhausted)
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]  # Swap 0 to the front
            low += 1                  # Expand the 0-region
            mid += 1                  # Element at mid is now 1 (came from low region) — safe to advance

        elif nums[mid] == 1:
            mid += 1                  # 1 is already in the right place — just advance

        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]  # Swap 2 to the back
            high -= 1                 # Expand the 2-region
                                      # NOTE: do NOT advance mid — the swapped element is unknown


# --- General 3-way partition (generalized Dutch National Flag) ---
def partition_three_way(nums: list[int], pivot: int) -> None:
    """Partition nums into [< pivot | == pivot | > pivot] in O(N) time, O(1) space."""
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] < pivot:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == pivot:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```

**Key decisions to customize**:
- The three regions map to your three categories (less than / equal to / greater than pivot)
- The critical subtlety: when swapping from `high`, do NOT advance `mid` — the swapped element is unknown
- When swapping from `low`, DO advance `mid` — the swapped element came from the processed region (it's a 1)
- Extend to 4-way partition for 4Sum-style problems (rare in interviews)

**Complexity**: Time O(N), Space O(1)

---

## ⚡ Variations

| Sub-Pattern | Pointer Movement | When to Use | Key Invariant | Example Problems |
|---|---|---|---|---|
| **Opposite Direction** | Both inward from ends | Sorted array, pair finding, palindrome | `left < right`; sorted order enables elimination | LC #167 Two Sum II, LC #125 Valid Palindrome, LC #11 Container With Water |
| **Same Direction (slow/fast)** | Fast always advances; slow advances conditionally | In-place removal, deduplication, partitioning | `[0..slow]` is the "clean" prefix | LC #26 Remove Duplicates, LC #283 Move Zeroes, LC #977 Squares |
| **Partition (3-pointer)** | low/mid/high with 3 regions | 3-valued array, Dutch National Flag | `[0..low-1]=A`, `[low..mid-1]=B`, `[high+1..n-1]=C` | LC #75 Sort Colors |
| **Three Pointers (3Sum)** | Outer loop fixes one; inner pair is opposite-direction | Triplet/quadruplet finding | Sort first; skip duplicates at outer and inner levels | LC #15 3Sum, LC #16 3Sum Closest, LC #18 4Sum |

---

## 🏋️ Practice Problems (Ordered by Difficulty)

### 🟢 Easy

| # | Problem | Difficulty | Sub-Pattern | Hint |
|---|---------|-----------|-------------|------|
| 1 | [LC #125 Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | 🟢 Easy | Opposite Direction | Opposite pointers; skip non-alphanumeric with inner while loops. Compare `s[left].lower() == s[right].lower()`. |
| 2 | [LC #283 Move Zeroes](https://leetcode.com/problems/move-zeroes/) | 🟢 Easy | Same Direction | `slow` = next write position. Swap `nums[fast]` into `slow` when `nums[fast] != 0`. Swap (not assign) to push zeros back. |
| 3 | [LC #977 Squares of Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | 🟢 Easy | Same Direction (outside-in) | Largest squares are at the extremes. Fill result from back. Compare `nums[left]²` vs `nums[right]²`, place larger at `result[pos--]`. |

### 🟡 Medium

| # | Problem | Difficulty | Sub-Pattern | Hint |
|---|---------|-----------|-------------|------|
| 4 | [LC #167 Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | 🟡 Medium | Opposite Direction | Classic template. Sorted input → opposite pointers. If sum < target: `left++`. If sum > target: `right--`. Return 1-indexed. |
| 5 | [LC #15 3Sum](https://leetcode.com/problems/3sum/) | 🟡 Medium | Three Pointers | Sort first. Fix `nums[i]`, run opposite-direction on `[i+1..n-1]`. Skip duplicates at both the outer loop (`nums[i] == nums[i-1]`) and after finding a triplet. |
| 6 | [LC #11 Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 Medium | Opposite Direction | Area = `min(h[L], h[R]) * (R - L)`. Always move the **shorter** pointer inward — moving the taller one can only decrease area. |
| 7 | [LC #75 Sort Colors](https://leetcode.com/problems/sort-colors/) | 🟡 Medium | Partition (3-pointer) | Dutch National Flag. Three pointers: `low`, `mid`, `high`. When swapping from `high`, don't advance `mid`. One pass, O(1) space. |
| 8 | [LC #16 3Sum Closest](https://leetcode.com/problems/3sum-closest/) | 🟡 Medium | Three Pointers | Same structure as 3Sum. Track `closest = float('inf')`. Update when `abs(total - target) < abs(closest - target)`. |

### 🔴 Hard

| # | Problem | Difficulty | Sub-Pattern | Hint |
|---|---------|-----------|-------------|------|
| 9 | [LC #42 Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | 🔴 Hard | Opposite Direction | Track `left_max` and `right_max`. Process the side with the smaller max: `water += max_side - height[pointer]`. The smaller max is the true bottleneck. |
| 10 | [LC #18 4Sum](https://leetcode.com/problems/4sum/) | 🔴 Hard | Three Pointers (extended) | Two nested loops fix `nums[i]` and `nums[j]`; inner opposite-direction finds the pair. Sort first. Skip duplicates at all three levels. Watch for integer overflow with large values. |

---

## 🔗 Related Patterns

| Pattern | Relationship | When to Switch |
|---|---|---|
| **Sliding Window** | Same-direction variant with a maintained window between the two pointers | Problem involves a **contiguous subarray** with a running constraint (sum ≤ K, at most K distinct chars) → use Sliding Window |
| **Binary Search** | Also exploits sorted arrays, but for single-element search | Need to find **one element** (not a pair) in a sorted array, or the answer space is monotonic → use Binary Search |
| **Hash Map** | Unsorted-array alternative to opposite-direction two pointers | Array is **unsorted** and sorting would lose information → use Hash Map for O(N) pair finding at O(N) space cost |
| **Fast & Slow Pointers** | Same-direction concept applied to linked lists | Working with a **linked list** (cycle detection, finding middle, nth from end) → use Floyd's algorithm |

---

## 📊 Complexity Summary

| Template | Time | Space | Notes |
|---|---|---|---|
| Opposite Direction (pair finding) | O(N) | O(1) | Requires sorted input; each pointer moves at most N times |
| Opposite Direction (palindrome) | O(N) | O(1) | Inner while loops still O(N) total across all iterations |
| Same Direction (slow/fast) | O(N) | O(1) | Fast pointer visits each element exactly once |
| Squares of Sorted Array | O(N) | O(N) | Output array required; pointers move inward from both ends |
| Partition (Dutch National Flag) | O(N) | O(1) | Single pass; mid processes each element at most once |
| Three Pointers (3Sum) | O(N²) | O(1) | Outer loop O(N) × inner two-pointer O(N); sort is O(N log N) |
| Three Pointers (4Sum) | O(N³) | O(1) | Two outer loops O(N²) × inner two-pointer O(N) |

---

## 🧪 Quick Self-Test

Before moving on, make sure you can:
- [ ] Write the opposite-direction Two Sum II template from memory in < 2 minutes
- [ ] Explain why you move the **shorter** pointer in Container With Most Water (not the taller one)
- [ ] Explain the Dutch National Flag invariant and why you don't advance `mid` after swapping from `high`
- [ ] Write the 3Sum solution including duplicate-skipping logic at both the outer and inner levels
- [ ] Explain the Trapping Rain Water two-pointer approach: why processing the smaller-max side is correct
- [ ] Identify which sub-pattern (opposite, same-direction, partition, three-pointer) applies to each of the 10 practice problems
