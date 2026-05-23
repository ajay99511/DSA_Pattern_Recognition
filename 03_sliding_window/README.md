# Sliding Window

> **Module 03 of 16** | Phase 2: Linear Patterns | Week 3–4
>
> Master the art of processing contiguous subarrays in O(N) — eliminate redundant recomputation by maintaining a live window that expands and contracts as you slide across the input.

---

## 🎯 When to Use This Pattern

**Signal words** (any of these in the problem → think Sliding Window first):

- `"contiguous subarray"` / `"contiguous substring"` → classic window problem
- `"maximum/minimum sum of size K"` / `"average of subarray of size K"` → fixed window
- `"longest substring with at most K distinct characters"` → variable window
- `"longest substring without repeating characters"` → variable window + set
- `"permutation in string"` / `"anagram in string"` → fixed window + frequency match
- `"minimum window containing all characters"` → variable window, shrink to minimize
- `"at most K replacements"` / `"at most K zeros"` → variable window with budget
- `"sliding window maximum/minimum"` → fixed window + monotonic deque
- `"number of subarrays with sum equal to K"` → variable window or prefix sum

**Input characteristics that suggest this pattern**:

- Input is an **array or string** (linear, indexable)
- Problem asks about a **contiguous** portion — not any subsequence
- There is a **constraint** on the window (size = K, sum ≤ target, at most K distinct, etc.)
- Brute force is O(N²) or O(N²·K) — sliding window reduces it to O(N)
- The constraint is **monotonic**: if a window is invalid, making it larger keeps it invalid (variable window shrink); if a window is valid, making it larger keeps it valid (variable window expand)

**When NOT to use**:

- Elements don't need to be **contiguous** → prefer DP or Two Pointers on sorted input
- You need **all pairs** (not a window) → prefer Hash Map or Two Pointers
- The window constraint is **non-monotonic** (e.g., "exactly K distinct") → split into "at most K" minus "at most K−1"
- Input is a **linked list** → prefer Fast & Slow Pointers
- You need **global** max/min across the whole array → prefer a single pass

---

## 🧠 Core Concept

### Why Sliding Window beats O(N²) brute force

The brute-force approach to "find the maximum sum subarray of size K" recomputes the sum from scratch for every window:

```
for i in range(n - k + 1):
    window_sum = sum(nums[i:i+k])   # O(K) per window → O(N·K) total — too slow
```

Sliding window exploits the **overlap** between consecutive windows. When you slide one position to the right, only one element enters and one element leaves:

```
Window [i .. i+k-1] → Window [i+1 .. i+k]
  Remove: nums[i]
  Add:    nums[i+k]
  Cost:   O(1) per slide → O(N) total
```

**The key insight**: instead of recomputing the window from scratch, maintain a running state (sum, frequency map, set, deque) and update it incrementally as the window moves.

### Visual: Fixed Window sliding across an array

```
nums = [2, 1, 5, 1, 3, 2],  k = 3

Step 0:  [2  1  5] 1  3  2   window_sum = 8
          L     R

Step 1:   2 [1  5  1] 3  2   window_sum = 8 - 2 + 1 = 7
             L     R

Step 2:   2  1 [5  1  3] 2   window_sum = 7 - 1 + 3 = 9  ← max
                L     R

Step 3:   2  1  5 [1  3  2]  window_sum = 9 - 5 + 2 = 6
                   L     R

Answer: 9
```

### Visual: Variable Window expanding and shrinking

```
s = "abcabcbb",  find longest substring without repeating chars

right →  a  b  c  a  b  c  b  b
         ↑
left=0   [a]                        window="a",  len=1
         [a  b]                     window="ab", len=2
         [a  b  c]                  window="abc",len=3  ← max so far
         [a  b  c  a] ← 'a' repeats!
            [b  c  a]  shrink: remove 'a' from left
            [b  c  a  b] ← 'b' repeats!
               [c  a  b]  shrink: remove 'b' from left
               [c  a  b  c] ← 'c' repeats!
                  [a  b  c]  shrink: remove 'c' from left
                  [a  b  c  b] ← 'b' repeats!
                     [b  c  b] → [c  b]  shrink twice
                        [c  b  b] ← 'b' repeats!
                           [b]  shrink

Answer: 3  (window "abc")
```

### The two fundamental modes

**Fixed Window**: window size `k` is constant. Slide by adding `nums[right]` and removing `nums[right - k]`. The window never shrinks — it just slides.

**Variable Window**: window size changes. Expand `right` to explore; shrink `left` when the constraint is violated (or to minimize the window after it becomes valid). The window grows and shrinks dynamically.

---

## 📐 Template Code (Python)

### Template 1: Fixed Window — window size k is constant

Use when: problem gives you a fixed window size K, asks for max/min/average/count over all windows of size K.

```python
def fixed_window(nums: list[int], k: int) -> int:
    # ── Step 1: Build the initial window ──────────────────────────────────
    window_sum = sum(nums[:k])          # Seed the window with the first k elements
    result = window_sum                 # Initialize result with the first window

    # ── Step 2: Slide the window one position at a time ───────────────────
    for i in range(k, len(nums)):
        window_sum += nums[i]           # Add the incoming element (right edge)
        window_sum -= nums[i - k]       # Remove the outgoing element (left edge)
                                        # nums[i - k] is exactly k positions behind nums[i]
        result = max(result, window_sum)  # Update result (change max→min for minimum problems)

    return result


# ── Variant: Fixed window with frequency tracking (anagram / permutation) ──
def fixed_window_freq(s: str, p: str) -> list[int]:
    """Find all starting indices where an anagram of p appears in s. (LC #438)"""
    from collections import Counter

    if len(p) > len(s):
        return []

    p_count = Counter(p)                # Target frequency map
    window = Counter(s[:len(p)])        # Frequency map of the first window
    result = []

    if window == p_count:               # Check the first window
        result.append(0)

    for i in range(len(p), len(s)):
        # Slide: add incoming character
        window[s[i]] += 1

        # Slide: remove outgoing character (the one that just left the window)
        outgoing = s[i - len(p)]
        window[outgoing] -= 1
        if window[outgoing] == 0:
            del window[outgoing]        # Keep Counter clean — don't leave zero-count keys

        if window == p_count:           # O(26) comparison for lowercase letters
            result.append(i - len(p) + 1)

    return result
```

**Key decisions to customize**:
- Change `max(result, window_sum)` to `min` for minimum problems
- Replace `window_sum` with a `Counter` or `set` for character-based windows
- The outgoing element is always `nums[i - k]` — the element exactly `k` positions behind the current right edge
- For average: return `window_sum / k` at each step

**Complexity**: Time O(N), Space O(1) for numeric windows; O(Σ) for character windows (Σ = alphabet size)

---

### Template 2: Variable Window (expand/shrink) — find longest window satisfying a condition

Use when: find the **longest** subarray/substring satisfying a constraint. Expand `right` always; shrink `left` when the constraint is violated.

```python
def variable_window_longest(s: str, k: int) -> int:
    """
    Generic template: find the longest window with at most k 'bad' elements.
    Customize: replace the constraint check and the window state update.
    """
    from collections import defaultdict

    freq = defaultdict(int)             # Window state: frequency of each character
    left = 0
    max_len = 0

    for right in range(len(s)):
        # ── Expand: add s[right] to the window ────────────────────────────
        freq[s[right]] += 1

        # ── Shrink: while the window violates the constraint, move left ───
        # CUSTOMIZE THIS CONDITION for your specific problem:
        #   - "at most k distinct chars":  while len(freq) > k
        #   - "no repeating chars":        while freq[s[right]] > 1
        #   - "at most k replacements":    while (right-left+1) - max(freq.values()) > k
        while len(freq) > k:            # ← replace with your constraint
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]       # Remove exhausted keys to keep len(freq) accurate
            left += 1                   # Shrink from the left

        # ── Update answer: window [left..right] is now valid ──────────────
        max_len = max(max_len, right - left + 1)

    return max_len


# ── Concrete example: LC #3 Longest Substring Without Repeating Characters ──
def length_of_longest_substring(s: str) -> int:
    seen = set()                        # Track characters currently in the window
    left = 0
    max_len = 0

    for right in range(len(s)):
        # Shrink until s[right] is no longer a duplicate
        while s[right] in seen:
            seen.remove(s[left])        # Remove the leftmost character
            left += 1

        seen.add(s[right])              # Now s[right] is safe to add
        max_len = max(max_len, right - left + 1)

    return max_len


# ── Concrete example: LC #1004 Max Consecutive Ones III ──────────────────────
def longest_ones(nums: list[int], k: int) -> int:
    """Flip at most k zeros. Find the longest subarray of 1s after flipping."""
    left = 0
    zeros_in_window = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros_in_window += 1        # Expand: count the zero we just included

        while zeros_in_window > k:      # Constraint violated: too many zeros
            if nums[left] == 0:
                zeros_in_window -= 1    # Shrink: uncounting the zero we're removing
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

**Key decisions to customize**:
- The `while` condition is the heart of the template — it defines your constraint
- Use `while` (not `if`) because a single shrink step may not restore validity
- After the `while` loop, the window `[left..right]` is **guaranteed valid** — safe to update `max_len`
- For "exactly K" problems: `f(exactly K) = f(at most K) - f(at most K-1)`

**Complexity**: Time O(N) — `right` advances N times, `left` advances at most N times total; Space O(Σ) for the frequency map

---

### Template 3: Variable Window with Hash Map — find minimum window satisfying a condition

Use when: find the **shortest** window that satisfies a condition. Expand `right` to find a valid window; then shrink `left` as much as possible while the window stays valid.

```python
def variable_window_shortest(s: str, t: str) -> str:
    """
    Generic template: find the minimum window containing all required elements.
    LC #76 Minimum Window Substring.
    """
    from collections import Counter

    if not t or not s:
        return ""

    # ── Setup: what we need vs. what we have ──────────────────────────────
    need = Counter(t)                   # Required character frequencies
    missing = len(t)                    # Total characters still needed (decrements to 0 when valid)
    left = 0
    best_start = 0
    best_len = float('inf')

    for right, char in enumerate(s):
        # ── Expand: add s[right] to the window ────────────────────────────
        if need[char] > 0:              # This character is still needed
            missing -= 1               # One fewer character needed
        need[char] -= 1                # Decrement (can go negative — means we have excess)

        # ── Shrink: while the window is valid, try to minimize it ─────────
        while missing == 0:            # Window contains all required characters
            # Record this valid window if it's the best so far
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_start = left

            # Try to shrink from the left
            need[s[left]] += 1         # "Un-add" the leftmost character
            if need[s[left]] > 0:      # We actually needed that character
                missing += 1           # Window is now invalid — exit the while loop
            left += 1                  # Advance left regardless

    return s[best_start : best_start + best_len] if best_len != float('inf') else ""


# ── Variant: LC #209 Minimum Size Subarray Sum ───────────────────────────────
def min_subarray_len(target: int, nums: list[int]) -> int:
    """Find the minimum length subarray with sum ≥ target."""
    left = 0
    window_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        window_sum += nums[right]       # Expand: add the new element

        while window_sum >= target:     # Window is valid: try to shrink
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]    # Remove the leftmost element
            left += 1                   # Shrink from the left

    return min_len if min_len != float('inf') else 0
```

**Key decisions to customize**:
- The `missing` counter is the key trick for multi-character matching — it tracks how many characters are still unsatisfied
- `need[char]` can go negative (excess copies) — only `need[char] > 0` means we actually need it
- The inner `while` loop runs the shrink phase — it fires only when the window is valid
- For numeric sums: replace `need`/`missing` with `window_sum` and a simple `>=` check

**Complexity**: Time O(N + |t|), Space O(|t| + Σ) — each pointer moves at most N times

---

## ⚡ Variations

| Sub-Pattern | Recognition Signal | Window State | Template to Use | Example Problems |
|---|---|---|---|---|
| **Fixed Window** | "size K", "window of length K", "subarray of size K" | Running sum, Counter, or set of size K | Template 1 | LC #643, LC #1343, LC #567, LC #438 |
| **Variable Window — Longest** | "longest substring/subarray", "at most K distinct/zeros/replacements" | freq map or counter; shrink when violated | Template 2 | LC #3, LC #424, LC #1004 |
| **Variable Window — Shortest** | "minimum window", "smallest subarray with sum ≥ target" | need/missing counter or running sum; shrink while valid | Template 3 | LC #76, LC #209 |
| **Fixed Window + Monotonic Deque** | "maximum/minimum of each window of size K" | Deque of indices (decreasing values for max) | Template 1 + Deque | LC #239 |
| **Exactly K (split trick)** | "exactly K distinct", "exactly K occurrences" | Two calls to "at most K" template | Template 2 × 2 | LC #992 Subarrays with K Different Integers |
| **Two-String Window** | "permutation in string", "anagram", "contains all chars of t" | Counter comparison or need/missing | Template 1 or 3 | LC #567, LC #438, LC #76 |

---

## 🏋️ Practice Problems (Ordered by Difficulty)

### 🟢 Easy

| # | Problem | Difficulty | Sub-Pattern | Hint |
|---|---------|-----------|-------------|------|
| 1 | [LC #643 Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | 🟢 Easy | Fixed Window | Seed with `sum(nums[:k])`. Slide: `+nums[i] - nums[i-k]`. Return `max_sum / k`. Watch for float division. |
| 2 | [LC #1343 Number of Sub-arrays of Size K and Average ≥ Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) | 🟢 Easy | Fixed Window | Fixed window of size K. Count windows where `window_sum / k >= threshold`. Equivalently: `window_sum >= threshold * k` (avoids float). |

### 🟡 Medium

| # | Problem | Difficulty | Sub-Pattern | Hint |
|---|---------|-----------|-------------|------|
| 3 | [LC #3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟡 Medium | Variable Window — Longest | Use a `set` to track chars in window. When `s[right]` is already in the set, shrink from left until it's removed. `max_len = right - left + 1`. |
| 4 | [LC #424 Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | 🟡 Medium | Variable Window — Longest | Window is valid when `(window_size - max_freq) <= k`. Track `max_freq` with a Counter. Shrink when invalid. Key insight: `max_freq` never needs to decrease — only increasing it matters. |
| 5 | [LC #567 Permutation in String](https://leetcode.com/problems/permutation-in-string/) | 🟡 Medium | Fixed Window + Freq Match | Fixed window of `len(p)`. Compare `Counter(window) == Counter(p)`. Optimize: track a `matches` count instead of full Counter comparison each step. |
| 6 | [LC #438 Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | 🟡 Medium | Fixed Window + Freq Match | Same as LC #567 but collect all valid starting indices. Fixed window of `len(p)`. Append `i - len(p) + 1` when `window == p_count`. |
| 7 | [LC #209 Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | 🟡 Medium | Variable Window — Shortest | Expand right to accumulate sum. When `window_sum >= target`, record length and shrink from left. `min_len = min(min_len, right - left + 1)`. |
| 8 | [LC #1004 Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | 🟡 Medium | Variable Window — Longest | Track `zeros_in_window`. Expand right; if `nums[right] == 0`, increment counter. Shrink left when `zeros_in_window > k`. Answer is `right - left + 1`. |

### 🔴 Hard

| # | Problem | Difficulty | Sub-Pattern | Hint |
|---|---------|-----------|-------------|------|
| 9 | [LC #76 Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | 🔴 Hard | Variable Window — Shortest + Hash Map | Use `need` Counter and `missing` count. Expand right: if `need[char] > 0`, decrement `missing`. Shrink left while `missing == 0`. Record best window during shrink phase. |
| 10 | [LC #239 Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | 🔴 Hard | Fixed Window + Monotonic Deque | Maintain a **monotonic decreasing deque** of indices. Before adding `i`: pop indices outside window (`dq[0] < i - k + 1`), pop smaller values from back (`nums[dq[-1]] < nums[i]`). `dq[0]` is always the max. |

---

## 🔗 Related Patterns

| Pattern | Relationship | When to Switch |
|---|---|---|
| **Two Pointers** | Sliding window IS two pointers (`left` and `right`) with a maintained window between them. The difference is intent: two pointers typically converge from opposite ends on sorted input; sliding window expands/contracts on unsorted input. | Problem involves a **sorted array** and you're finding pairs → use Two Pointers (opposite direction). Problem involves a **contiguous subarray** with a running constraint → use Sliding Window. |
| **Hash Map** | Hash maps are the most common data structure *inside* a sliding window. They track character/element frequencies within the window, enabling O(1) constraint checks. | Hash maps are a tool *within* sliding window, not an alternative. If the problem has no contiguous constraint, use a standalone Hash Map (e.g., Two Sum). |
| **Monotonic Deque** | Required when the window needs its **maximum or minimum** in O(1). A plain sliding window can't answer "what's the max in this window?" efficiently — the deque maintains a sorted front-of-window invariant. | Whenever the problem asks for the max/min *of each window* (not just the overall max/min), add a monotonic deque to your sliding window. |
| **Prefix Sum** | Alternative to sliding window for **sum queries** on static arrays. Prefix sum answers "sum of subarray [i..j]" in O(1) after O(N) preprocessing. | If you need to answer **multiple** sum queries on the same array, prefix sum is better. If you're scanning once for an optimal window, sliding window is cleaner. |
| **Binary Search on Answer** | For problems like "minimum window with sum ≥ target", binary search on the answer length combined with a fixed-window check is an alternative O(N log N) approach. | Sliding window gives O(N) directly — prefer it. Binary search on answer is useful when the constraint is more complex and the monotonic property is harder to exploit directly. |

---

## 📊 Complexity Summary

| Template | Time | Space | Notes |
|---|---|---|---|
| Fixed Window (numeric) | O(N) | O(1) | Single pass; add/remove one element per step |
| Fixed Window (frequency) | O(N) | O(Σ) | Counter comparison is O(Σ) per step; Σ = alphabet size (26 for lowercase) |
| Variable Window — Longest | O(N) | O(Σ) | `right` advances N times; `left` advances at most N times total |
| Variable Window — Shortest | O(N) | O(Σ) | Same two-pointer argument; inner `while` is amortized O(1) per element |
| Fixed Window + Monotonic Deque | O(N) | O(K) | Each element pushed/popped from deque at most once |

---

## 🧪 Quick Self-Test

Before moving on, make sure you can:

- [ ] Write the fixed window template from memory in < 2 minutes — seed, slide, update
- [ ] Explain the difference between the "longest" and "shortest" variable window templates — when does the `while` loop fire in each?
- [ ] Explain why `max_freq` never needs to decrease in LC #424 (Longest Repeating Character Replacement)
- [ ] Explain the `missing` counter trick in LC #76 — why can `need[char]` go negative, and what does that mean?
- [ ] Explain the monotonic deque invariant for LC #239 — why do you pop from the back before adding a new element?
- [ ] Solve the "exactly K distinct" problem using the "at most K" minus "at most K−1" split trick
- [ ] Identify which sub-pattern (fixed, variable-longest, variable-shortest, deque) applies to each of the 10 practice problems
