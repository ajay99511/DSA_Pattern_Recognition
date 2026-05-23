# Arrays & Hashing

> **Module 01 of 16** | Phase 2: Linear Patterns | Week 3
>
> Master hash maps, frequency counting, and prefix sums — the foundation of O(N) solutions.

---

## 🎯 When to Use This Pattern

**Signal words** (any of these in the problem → think Arrays & Hashing first):
- `"find pair"` / `"find group"` → complement lookup
- `"count occurrences"` / `"frequency"` → frequency map
- `"subarray sum equals K"` → prefix sum + hash map
- `"two sum"` / `"target sum"` → complement lookup
- `"anagram"` / `"permutation of"` → frequency map / canonical key
- `"duplicate"` / `"contains duplicate"` → set for existence
- `"top K frequent"` / `"most common"` → Counter + heap
- `"product except self"` / `"prefix product"` → prefix/suffix arrays
- `"longest consecutive"` → set + sequence expansion

**Input characteristics that suggest this pattern**:
- Unsorted array where you need O(1) lookups (sorting would cost O(N log N))
- Need to count or track element frequencies
- Need to find pairs, groups, or elements matching a condition
- Cumulative / running aggregates over subarrays (range sum queries)
- Problem asks for O(N) time — hash map is usually the key
- Brute force is O(N²) — hash map typically reduces it to O(N)

**When NOT to use**:
- Array is already sorted → prefer Two Pointers (O(1) space)
- Need contiguous subarray with a constraint → prefer Sliding Window
- Need ordered traversal → prefer monotonic stack

---

## 🧠 Core Concept

### Hash Maps give O(1) average-case lookup

A Python `dict` (hash map) stores key-value pairs in a hash table. Lookup, insert, and delete are all **O(1) average** (O(N) worst case due to collisions, but rare in practice).

This single fact transforms many O(N²) brute-force solutions into O(N):

```
Brute force: for every element, scan the rest of the array → O(N²)
Hash map:    for every element, check the hash map → O(N)
```

### Why frequency counting works

When you need to know "how many times does X appear?", a `Counter` (or `defaultdict(int)`) builds a frequency map in O(N). Comparing two frequency maps is O(1) if the alphabet is fixed (e.g., 26 letters), making anagram checks O(N) instead of O(N log N).

```
Counter("anagram") == Counter("nagaram")  # True — O(N) check
```

### How prefix sums enable range queries

A prefix sum array `P` where `P[i] = nums[0] + nums[1] + ... + nums[i-1]` lets you answer "what is the sum of nums[i..j]?" in O(1):

```
sum(nums[i..j]) = P[j+1] - P[i]
```

Combined with a hash map, you can answer "how many subarrays sum to K?" in O(N) by tracking how many times each prefix sum has appeared.

---

## 📐 Template Code (Python)

### Template 1: Complement Lookup (Two Sum style)

Use when: "find two elements that satisfy a condition" (sum, difference, product).

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}                          # Maps value → index for O(1) lookup

    for i, num in enumerate(nums):
        complement = target - num      # What value do we NEED to complete the pair?

        if complement in seen:         # O(1) check — did we see the complement before?
            return [seen[complement], i]  # Found the pair; return both indices

        seen[num] = i                  # Store current value → index for future lookups
                                       # NOTE: store AFTER checking to avoid using same element twice

    return []                          # No pair found (problem guarantees one exists, so unreachable)
```

**Key decisions to customize**:
- Change `complement = target - num` to match your condition (e.g., `target // num` for product)
- Return indices vs. values depending on what the problem asks
- Use `seen.setdefault(num, i)` if you need the FIRST occurrence of a duplicate

**Complexity**: Time O(N), Space O(N)

---

### Template 2: Frequency Counting

Use when: "count occurrences", "group by property", "anagram check", "top K elements".

```python
from collections import Counter, defaultdict

# --- 2a: Simple frequency count ---
def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)    # Counter builds freq map in O(N); comparison is O(alphabet size)

# --- 2b: Group by canonical form ---
def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)         # Key: canonical form → Value: list of matching strings

    for s in strs:
        key = tuple(sorted(s))         # Canonical form: sorted characters as a hashable tuple
                                       # All anagrams share the same sorted form
        groups[key].append(s)          # Group strings by their canonical key

    return list(groups.values())       # Return all groups

# --- 2c: Top K frequent (Counter + heap) ---
import heapq

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)               # Build frequency map: value → count, O(N)

    # heapq.nlargest uses a min-heap of size k internally → O(N log k)
    return heapq.nlargest(k, freq.keys(), key=freq.get)
    # Alternative: bucket sort for O(N) — see templates.py
```

**Key decisions to customize**:
- Choose canonical form based on problem: `sorted(s)` for anagrams, `frozenset` for sets, custom tuple for other groupings
- Use `Counter.most_common(k)` for top-K without heapq
- Use `defaultdict(int)` when you need to increment counts manually

**Complexity**: Time O(N) or O(N log N) for sorted key, Space O(N)

---

### Template 3: Prefix Sum

Use when: "subarray sum equals K", "range sum query", "number of subarrays with property".

```python
def subarray_sum(nums: list[int], k: int) -> int:
    prefix_count = {0: 1}             # Maps prefix_sum → number of times it has appeared
                                       # Initialize with {0: 1} to handle subarrays starting at index 0

    curr_sum = 0                       # Running prefix sum
    result = 0                         # Count of valid subarrays

    for num in nums:
        curr_sum += num                # Extend prefix sum to include current element

        # Key insight: if (curr_sum - k) appeared before at index j,
        # then nums[j+1..i] sums to k
        needed = curr_sum - k
        result += prefix_count.get(needed, 0)  # Add count of times (curr_sum - k) appeared

        # Record this prefix sum for future iterations
        prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

    return result

# --- Static prefix sum array (for multiple range queries) ---
def build_prefix(nums: list[int]) -> list[int]:
    prefix = [0] * (len(nums) + 1)    # prefix[0] = 0 (empty prefix)
    for i, num in enumerate(nums):
        prefix[i + 1] = prefix[i] + num  # prefix[i+1] = sum of nums[0..i]
    return prefix

def range_sum(prefix: list[int], left: int, right: int) -> int:
    return prefix[right + 1] - prefix[left]  # Sum of nums[left..right] in O(1)
```

**Key decisions to customize**:
- Change `needed = curr_sum - k` for different conditions (e.g., `curr_sum % k == 0` → track `curr_sum % k`)
- For 2D prefix sums (matrix range queries), extend to `prefix[i][j]`
- Use `itertools.accumulate(nums)` for a one-liner prefix sum list

**Complexity**: Time O(N), Space O(N)

---

## ⚡ Variations

| Sub-Pattern | When to Use | Key Data Structure | Example Problem |
|---|---|---|---|
| **Complement Lookup** | Find pair/triple satisfying a condition | `dict` (value → index) | LC #1 Two Sum |
| **Frequency Map** | Count occurrences, group by property | `Counter` / `defaultdict(int)` | LC #242 Valid Anagram, LC #347 Top K |
| **Prefix Sum** | Subarray sum queries, range aggregates | `dict` (prefix → count) + running sum | LC #560 Subarray Sum = K |
| **Set for Existence** | Just need True/False membership check | `set` | LC #217 Contains Duplicate, LC #128 Consecutive |
| **Sliding Window + Hash Map** | Variable-length window with frequency constraint | `dict` + two pointers | LC #3 Longest Substring Without Repeat |

---

## 🏋️ Practice Problems (Ordered by Difficulty)

### 🟢 Easy

| # | Problem | Difficulty | Pattern | Hint |
|---|---------|-----------|---------|------|
| 1 | [LC #217 Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | 🟢 Easy | Set for Existence | Add to set; if already present → duplicate. O(N) time, O(N) space. |
| 2 | [LC #242 Valid Anagram](https://leetcode.com/problems/valid-anagram/) | 🟢 Easy | Frequency Map | `Counter(s) == Counter(t)`. Edge case: different lengths → False immediately. |
| 3 | [LC #1 Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | Complement Lookup | Store `value → index` in dict. For each num, check if `target - num` is already stored. |

### 🟡 Medium

| # | Problem | Difficulty | Pattern | Hint |
|---|---------|-----------|---------|------|
| 4 | [LC #49 Group Anagrams](https://leetcode.com/problems/group-anagrams/) | 🟡 Medium | Frequency Map + Canonical Key | Use `tuple(sorted(s))` as dict key. All anagrams map to the same key. |
| 5 | [LC #347 Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | 🟡 Medium | Frequency Map + Heap | `Counter` + `heapq.nlargest(k, ...)`. Bucket sort gives O(N). |
| 6 | [LC #238 Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | 🟡 Medium | Prefix/Suffix Product | Build left-product prefix, then multiply right-product suffix in-place. No division needed. |
| 7 | [LC #560 Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | 🟡 Medium | Prefix Sum + Hash Map | Track `prefix_sum → count`. For each position, check if `curr_sum - k` was seen before. |
| 8 | [LC #128 Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | 🟡 Medium | Set for Existence | Convert to set. Only start counting from sequence starts (`n-1 not in set`). O(N) total. |

### 🔴 Hard

| # | Problem | Difficulty | Pattern | Hint |
|---|---------|-----------|---------|------|
| 9 | [LC #36 Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | 🔴 Hard | Set for Existence (multi-dimensional) | Three sets: rows, cols, boxes. Box index = `(r//3, c//3)`. Single pass O(81). |
| 10 | [LC #271 Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | 🔴 Hard | Custom Encoding | Length-prefix encoding: `"4#word"`. Decoder reads length, skips `#`, reads exactly that many chars. |
| 11 | [LC #41 First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | 🔴 Hard | Array as Hash Map | Use the array itself as a hash map. Place `num` at index `num-1`. Answer is first index where `nums[i] != i+1`. O(N) time, O(1) extra space. |

---

## 🔗 Related Patterns

| Pattern | Relationship | When to Switch |
|---|---|---|
| **Two Pointers** | Sorted-array alternative to hash map | Array is sorted → two pointers saves O(N) space |
| **Sliding Window** | Extends hash map to variable-length windows | Problem involves contiguous subarray with a frequency/count constraint |
| **Dynamic Programming** | Prefix sum is a 1D DP recurrence | When you need more than just sums (e.g., max subarray) → Kadane's algorithm |
| **Sorting** | Pre-processing step before hashing | When canonical form requires sort (Group Anagrams), or when order matters |

---

## 📊 Complexity Summary

| Template | Time | Space | Notes |
|---|---|---|---|
| Complement Lookup | O(N) | O(N) | One pass; hash map stores up to N entries |
| Frequency Counting | O(N) | O(K) | K = number of distinct elements |
| Prefix Sum + Hash | O(N) | O(N) | One pass; hash map stores prefix sums |
| Set for Existence | O(N) | O(N) | Set stores up to N elements |
| Sliding Window + Hash | O(N) | O(K) | K = window constraint (e.g., alphabet size) |

---

## 🧪 Quick Self-Test

Before moving on, make sure you can:
- [ ] Write the Two Sum solution from memory in < 2 minutes
- [ ] Explain why `prefix_count = {0: 1}` is initialized in the prefix sum template
- [ ] Identify which sub-pattern applies to each of the 11 practice problems
- [ ] Explain the O(N) trick for First Missing Positive (array as hash map)
- [ ] Describe when to use `Counter` vs `defaultdict(int)` vs plain `dict`
