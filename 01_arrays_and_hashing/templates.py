"""
Arrays & Hashing — Reusable Templates
======================================
Four core O(N) patterns that eliminate brute-force O(N²) solutions:

  1. Hash Map Complement  — find pairs/groups satisfying a condition
  2. Frequency Counting   — count occurrences, group by property, top-K
  3. Prefix Sum           — subarray sums, range queries, 2D matrix queries
  4. Set for Existence    — duplicate detection, consecutive sequences, missing values

Each template includes:
  • WHY each line exists (not just what it does)
  • Complexity analysis (time + space)
  • Runnable assertions that verify correctness

Run with:  python templates.py
"""

from collections import defaultdict, Counter
from typing import List
import heapq
from itertools import accumulate


# ============================================================
# TEMPLATE 1: HASH MAP COMPLEMENT LOOKUP
# ============================================================
#
# CORE IDEA: Instead of scanning the rest of the array for a matching
# element (O(N) per element → O(N²) total), store what you've already
# seen in a hash map so each lookup is O(1).
#
# SIGNAL WORDS: "find pair", "two sum", "target sum", "find two numbers"
# TIME: O(N)  |  SPACE: O(N)
# ============================================================


def two_sum_indices(nums: List[int], target: int) -> List[int]:
    """
    LC #1 — Return the INDICES of the two numbers that add to target.

    WHY hash map: brute force checks every pair → O(N²).
    Hash map lets us answer "have I seen the complement?" in O(1).

    Complexity: Time O(N) — one pass.  Space O(N) — map stores up to N entries.
    """
    seen = {}                           # WHY: maps value → index so we can retrieve the index of the complement

    for i, num in enumerate(nums):
        complement = target - num       # WHY: if num + complement == target, we need to find complement

        if complement in seen:          # WHY: O(1) hash map lookup — did we already encounter the complement?
            return [seen[complement], i]  # WHY: return both indices; seen[complement] is the earlier index

        seen[num] = i                   # WHY: store AFTER checking to avoid using the same element twice
                                        #      (e.g., target=6, num=3 — we don't want to pair index 0 with itself)

    return []                           # WHY: problem guarantees exactly one solution, so this is unreachable


def two_sum_values(nums: List[int], target: int) -> List[int]:
    """
    Variant — Return the VALUES (not indices) of the two numbers.

    WHY separate variant: many problems ask for values, not indices.
    The logic is identical; only the return statement changes.

    Complexity: Time O(N).  Space O(N).
    """
    seen = set()                        # WHY: we only need membership check, not index → set is sufficient

    for num in nums:
        complement = target - num       # WHY: same complement logic — what value completes the pair?

        if complement in seen:          # WHY: O(1) set lookup
            return [complement, num]    # WHY: return the two values that sum to target

        seen.add(num)                   # WHY: record this value for future complement checks

    return []


def find_pair_with_difference(nums: List[int], k: int) -> List[int]:
    """
    Generic complement pattern — find two numbers where |a - b| == k.

    WHY this generalises: the complement formula changes (target - num → num + k or num - k),
    but the hash map structure is identical.

    Complexity: Time O(N).  Space O(N).
    """
    num_set = set(nums)                 # WHY: build lookup set in one pass before searching

    for num in nums:
        # WHY check both directions: num could be the smaller or larger of the pair
        if num + k in num_set and num + k != num:   # avoid pairing num with itself when k==0
            return [num, num + k]
        if num - k in num_set and num - k != num:
            return [num - k, num]

    return []


# ============================================================
# TEMPLATE 2: FREQUENCY COUNTING
# ============================================================
#
# CORE IDEA: Build a frequency map (value → count) in O(N), then
# answer questions about counts in O(1) per query.
#
# SIGNAL WORDS: "count occurrences", "frequency", "anagram",
#               "top K frequent", "group by property"
# TIME: O(N)  |  SPACE: O(K) where K = distinct elements
# ============================================================


def is_anagram(s: str, t: str) -> bool:
    """
    LC #242 — True if t is an anagram of s.

    WHY Counter: builds frequency map in O(N); equality check is O(alphabet size) = O(1) for fixed alphabet.
    WHY not sort: sorting is O(N log N) — Counter is strictly faster.

    Complexity: Time O(N).  Space O(1) — at most 26 lowercase letters.
    """
    if len(s) != len(t):               # WHY: different lengths → can't be anagrams; early exit saves work
        return False

    return Counter(s) == Counter(t)    # WHY: Counter builds {char: count} maps; equal maps ↔ same characters


def frequency_map_manual(nums: List[int]) -> dict:
    """
    Manual frequency counting with defaultdict(int).

    WHY defaultdict(int): avoids KeyError on first access — missing keys default to 0.
    WHY use this over Counter: when you need to increment conditionally or track custom values.

    Complexity: Time O(N).  Space O(K).
    """
    freq = defaultdict(int)            # WHY defaultdict(int): freq[x] starts at 0 automatically

    for num in nums:
        freq[num] += 1                 # WHY: increment count; no need to check if key exists first

    return dict(freq)                  # WHY: convert to plain dict for clean return type


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    LC #49 — Group strings that are anagrams of each other.

    WHY canonical key: all anagrams share the same sorted character sequence.
    Sorting each string gives a unique "fingerprint" that groups anagrams together.

    WHY defaultdict(list): automatically creates an empty list for new keys.

    Complexity: Time O(N * M log M) where M = avg string length (for sorting).
                Space O(N * M) — storing all strings in groups.
    """
    groups = defaultdict(list)         # WHY: maps canonical_key → [list of anagrams]

    for s in strs:
        key = tuple(sorted(s))         # WHY tuple: sorted() returns a list; lists aren't hashable as dict keys
                                       # WHY sorted: all anagrams produce the same sorted sequence
        groups[key].append(s)          # WHY: add this string to its anagram group

    return list(groups.values())       # WHY: discard the keys; caller only needs the groups


def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    """
    LC #347 — Top K frequent elements using a min-heap.

    WHY heap: heapq.nlargest maintains a heap of size k → O(N log k).
    WHY not sort all: sorting all N elements is O(N log N); heap is faster when k << N.

    Complexity: Time O(N log k).  Space O(N) for the frequency map.
    """
    freq = Counter(nums)               # WHY: build frequency map first — O(N)

    # WHY heapq.nlargest: internally uses a min-heap of size k, evicting the smallest
    # as it scans, giving O(N log k) instead of O(N log N) for a full sort
    return heapq.nlargest(k, freq.keys(), key=freq.get)


def top_k_frequent_bucket_sort(nums: List[int], k: int) -> List[int]:
    """
    LC #347 — Top K frequent elements using bucket sort — O(N).

    WHY bucket sort: frequency can be at most N (if all elements are the same).
    Create N+1 buckets indexed by frequency; scan from high to low to get top-K.
    This avoids any comparison-based sorting → strictly O(N).

    Complexity: Time O(N).  Space O(N).
    """
    freq = Counter(nums)               # WHY: frequency map — O(N)

    # WHY len(nums)+1 buckets: max possible frequency is len(nums) (all elements identical)
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]

    for num, count in freq.items():
        buckets[count].append(num)     # WHY: place num in the bucket matching its frequency

    result = []
    for i in range(len(buckets) - 1, -1, -1):  # WHY reverse: highest frequency first
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:       # WHY early exit: stop as soon as we have k elements
                return result

    return result                      # WHY: fallback (k <= len(nums) guaranteed by problem)


# ============================================================
# TEMPLATE 3: PREFIX SUM
# ============================================================
#
# CORE IDEA: Precompute cumulative sums so any range sum query
# is answered in O(1) instead of O(N).
#
# KEY INSIGHT: sum(nums[i..j]) = prefix[j+1] - prefix[i]
#
# SIGNAL WORDS: "subarray sum equals K", "range sum query",
#               "number of subarrays with property", "cumulative"
# TIME: O(N) build + O(1) per query  |  SPACE: O(N)
# ============================================================


def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """
    LC #560 — Count subarrays whose elements sum to k.

    WHY prefix sum + hash map: a subarray nums[j+1..i] sums to k
    iff prefix[i+1] - prefix[j] == k, i.e., prefix[j] == prefix[i+1] - k.
    Tracking how many times each prefix sum has appeared lets us count
    valid subarrays in O(1) per element.

    WHY {0: 1}: a prefix sum of 0 "appeared once before index 0" — this
    handles subarrays that start at index 0 (where prefix[j] = 0).

    Complexity: Time O(N).  Space O(N) — hash map stores up to N distinct prefix sums.
    """
    prefix_count = {0: 1}              # WHY: seed with 0 → handles subarrays starting at index 0
    curr_sum = 0                       # WHY: running prefix sum; updated each iteration
    result = 0                         # WHY: accumulates the count of valid subarrays

    for num in nums:
        curr_sum += num                # WHY: extend prefix sum to include current element

        needed = curr_sum - k          # WHY: if this prefix sum appeared before at index j,
                                       #      then nums[j+1..current] sums to k

        result += prefix_count.get(needed, 0)  # WHY .get(..., 0): safely returns 0 if needed never appeared

        # WHY update AFTER querying: we don't want to count the current index as a valid j
        prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

    return result


def build_prefix_array(nums: List[int]) -> List[int]:
    """
    Build a static prefix sum array for repeated range queries.

    WHY static array: when you need to answer many range queries on the same array,
    build once in O(N) and answer each query in O(1).

    prefix[0] = 0 (empty prefix — makes the formula uniform for all ranges)
    prefix[i] = nums[0] + nums[1] + ... + nums[i-1]

    Complexity: Time O(N).  Space O(N).
    """
    n = len(nums)
    prefix = [0] * (n + 1)            # WHY n+1: prefix[0]=0 acts as a sentinel for the empty prefix

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]  # WHY: each entry extends the previous by one element

    return prefix


def range_sum_query(prefix: List[int], left: int, right: int) -> int:
    """
    O(1) range sum using a prebuilt prefix array.

    WHY prefix[right+1] - prefix[left]:
      prefix[right+1] = sum(nums[0..right])
      prefix[left]    = sum(nums[0..left-1])
      difference      = sum(nums[left..right])  ✓

    Complexity: Time O(1).  Space O(1).
    """
    return prefix[right + 1] - prefix[left]  # WHY +1 on right: prefix is 1-indexed relative to nums


def prefix_sum_2d(matrix: List[List[int]]) -> List[List[int]]:
    """
    Build a 2D prefix sum table for matrix range queries.

    WHY 2D prefix: sum of any rectangular submatrix can be computed in O(1)
    using inclusion-exclusion on four corner values.

    prefix[i][j] = sum of all elements in matrix[0..i-1][0..j-1]

    Inclusion-exclusion formula:
      sum(r1,c1 → r2,c2) = P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]

    Complexity: Time O(R*C) to build.  Space O(R*C).
    """
    if not matrix or not matrix[0]:
        return [[]]

    R, C = len(matrix), len(matrix[0])
    # WHY (R+1) x (C+1): extra row/col of zeros acts as boundary sentinel
    prefix = [[0] * (C + 1) for _ in range(R + 1)]

    for r in range(1, R + 1):
        for c in range(1, C + 1):
            # WHY this formula: inclusion-exclusion to avoid double-counting
            prefix[r][c] = (matrix[r-1][c-1]
                            + prefix[r-1][c]    # add row above
                            + prefix[r][c-1]    # add column to left
                            - prefix[r-1][c-1]) # subtract top-left corner (counted twice)

    return prefix


def range_sum_2d(prefix: List[List[int]], r1: int, c1: int, r2: int, c2: int) -> int:
    """
    O(1) rectangular sum query using a 2D prefix table.

    WHY inclusion-exclusion: the four corners of the prefix table encode
    overlapping rectangles; subtracting the two edges and adding back the
    corner gives exactly the rectangle we want.

    Complexity: Time O(1).  Space O(1).
    """
    return (prefix[r2+1][c2+1]         # WHY: full rectangle from (0,0) to (r2,c2)
            - prefix[r1][c2+1]         # WHY: subtract top strip above r1
            - prefix[r2+1][c1]         # WHY: subtract left strip left of c1
            + prefix[r1][c1])          # WHY: add back top-left corner (subtracted twice)


def product_except_self(nums: List[int]) -> List[int]:
    """
    LC #238 — Product of array except self, no division, O(N) time O(1) extra space.

    WHY two passes: left pass builds prefix products; right pass multiplies suffix products.
    WHY no division: problem constraint; also handles zeros correctly.

    Complexity: Time O(N).  Space O(1) extra (output array doesn't count).
    """
    n = len(nums)
    result = [1] * n                   # WHY initialise to 1: neutral element for multiplication

    # Left pass: result[i] = product of all elements to the LEFT of i
    prefix = 1
    for i in range(n):
        result[i] = prefix             # WHY: store running left-product before including nums[i]
        prefix *= nums[i]              # WHY: extend prefix to include nums[i] for the next iteration

    # Right pass: multiply result[i] by product of all elements to the RIGHT of i
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix            # WHY: combine left-product (already in result[i]) with right-product
        suffix *= nums[i]              # WHY: extend suffix to include nums[i] for the next (leftward) iteration

    return result


# ============================================================
# TEMPLATE 4: SET FOR EXISTENCE / UNIQUENESS
# ============================================================
#
# CORE IDEA: A Python set provides O(1) average membership testing.
# Use it when you only need to know IF something exists, not how many
# times or where.
#
# SIGNAL WORDS: "duplicate", "contains", "exists", "consecutive",
#               "missing", "first missing positive"
# TIME: O(N)  |  SPACE: O(N)
# ============================================================


def contains_duplicate(nums: List[int]) -> bool:
    """
    LC #217 — True if any value appears at least twice.

    WHY set: adding to a set is O(1); if the element is already present,
    we found a duplicate immediately without scanning the rest.

    Complexity: Time O(N).  Space O(N).
    """
    seen = set()                       # WHY set: O(1) add and membership check

    for num in nums:
        if num in seen:                # WHY check before adding: first duplicate triggers early return
            return True
        seen.add(num)                  # WHY: record this value for future checks

    return False                       # WHY: no duplicate found after full scan


def longest_consecutive_sequence(nums: List[int]) -> int:
    """
    LC #128 — Length of the longest consecutive sequence. O(N) time.

    WHY set + "start of sequence" trick: converting to a set gives O(1) lookups.
    Only start counting from the beginning of a sequence (num-1 not in set).
    This ensures each element is visited at most twice → O(N) total.

    WHY not sort: sorting is O(N log N); set approach is strictly O(N).

    Complexity: Time O(N).  Space O(N).
    """
    num_set = set(nums)                # WHY: O(1) membership checks; also deduplicates

    longest = 0

    for num in num_set:                # WHY iterate over set: avoids processing duplicates
        # WHY only start from sequence beginnings: if num-1 exists, num is not the start.
        # Starting from non-starts would recount sequences and inflate the time complexity.
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:  # WHY: extend sequence as far as it goes
                length += 1
            longest = max(longest, length)  # WHY: track the maximum length seen so far

    return longest


def first_missing_positive(nums: List[int]) -> int:
    """
    LC #41 — Smallest missing positive integer. O(N) time, O(1) extra space.

    WHY use the array itself as a hash map: the answer must be in [1, N+1].
    We can encode "number i exists" by making nums[i-1] negative.
    This avoids any extra data structure.

    STEP 1: Eliminate non-positives (replace with N+1 as a sentinel).
    STEP 2: For each value v in [1,N], negate nums[v-1] to mark v as present.
    STEP 3: First index with a positive value → that index+1 is missing.

    Complexity: Time O(N) — three linear passes.  Space O(1) extra.
    """
    n = len(nums)

    # Step 1: Replace non-positives with n+1 (out-of-range sentinel)
    # WHY: values ≤ 0 or > n can't be the answer; n+1 won't interfere with marking
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1            # WHY n+1: safely out of the [1,N] range we care about

    # Step 2: Mark presence of values in [1, N] by negating the value at the target index
    for i in range(n):
        val = abs(nums[i])             # WHY abs: the value may already be negative from a previous mark
        if 1 <= val <= n:
            idx = val - 1              # WHY val-1: value v maps to index v-1 (0-indexed)
            if nums[idx] > 0:          # WHY check positive: avoid double-negating (would undo the mark)
                nums[idx] = -nums[idx] # WHY negate: encodes "value val has been seen"

    # Step 3: First index with a positive value → that index+1 is the missing number
    for i in range(n):
        if nums[i] > 0:                # WHY positive: this index was never marked → i+1 is missing
            return i + 1

    return n + 1                       # WHY n+1: all values 1..N are present; answer is N+1


# ============================================================
# MAIN — Runnable assertions for all templates
# ============================================================

if __name__ == "__main__":

    # ── Template 1: Hash Map Complement ──────────────────────

    # two_sum_indices: basic case
    assert two_sum_indices([2, 7, 11, 15], 9) == [0, 1], "two_sum_indices basic"
    # two_sum_indices: complement appears later
    assert two_sum_indices([3, 2, 4], 6) == [1, 2], "two_sum_indices later complement"
    # two_sum_indices: same value used twice (different indices)
    assert two_sum_indices([3, 3], 6) == [0, 1], "two_sum_indices duplicate values"

    # two_sum_values: returns values not indices
    result = two_sum_values([2, 7, 11, 15], 9)
    assert sorted(result) == [2, 7], "two_sum_values basic"

    # find_pair_with_difference
    result = find_pair_with_difference([1, 5, 3, 4, 2], 2)
    assert abs(result[0] - result[1]) == 2, "find_pair_with_difference"

    print("✅ Template 1 (Hash Map Complement) — all assertions passed")

    # ── Template 2: Frequency Counting ───────────────────────

    # is_anagram
    assert is_anagram("anagram", "nagaram") is True,  "is_anagram True"
    assert is_anagram("rat", "car")         is False, "is_anagram False"
    assert is_anagram("a", "ab")            is False, "is_anagram different lengths"

    # frequency_map_manual
    freq = frequency_map_manual([1, 2, 2, 3, 3, 3])
    assert freq == {1: 1, 2: 2, 3: 3}, "frequency_map_manual"

    # group_anagrams
    groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort each group and the list of groups for deterministic comparison
    groups_sorted = sorted([sorted(g) for g in groups])
    assert groups_sorted == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]], "group_anagrams"

    # top_k_frequent_heap
    assert set(top_k_frequent_heap([1, 1, 1, 2, 2, 3], 2)) == {1, 2}, "top_k_frequent_heap"
    assert top_k_frequent_heap([1], 1) == [1], "top_k_frequent_heap single"

    # top_k_frequent_bucket_sort
    assert set(top_k_frequent_bucket_sort([1, 1, 1, 2, 2, 3], 2)) == {1, 2}, "top_k_bucket"
    assert top_k_frequent_bucket_sort([1], 1) == [1], "top_k_bucket single"

    print("✅ Template 2 (Frequency Counting) — all assertions passed")

    # ── Template 3: Prefix Sum ────────────────────────────────

    # subarray_sum_equals_k
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2,       "subarray_sum k=2"
    assert subarray_sum_equals_k([1, 2, 3], 3) == 2,       "subarray_sum k=3 (two subarrays)"
    assert subarray_sum_equals_k([1], 0) == 0,              "subarray_sum no match"
    assert subarray_sum_equals_k([-1, -1, 1], 0) == 1,     "subarray_sum negative numbers"

    # build_prefix_array + range_sum_query
    nums = [1, 2, 3, 4, 5]
    prefix = build_prefix_array(nums)
    assert prefix == [0, 1, 3, 6, 10, 15], "build_prefix_array"
    assert range_sum_query(prefix, 1, 3) == 9,  "range_sum [1..3] = 2+3+4"
    assert range_sum_query(prefix, 0, 4) == 15, "range_sum [0..4] full array"
    assert range_sum_query(prefix, 2, 2) == 3,  "range_sum single element"

    # product_except_self
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6], "product_except_self"
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0], "product_except_self with zero"

    # 2D prefix sum
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
    p2d = prefix_sum_2d(matrix)
    # Sum of submatrix (2,1) to (4,3) should be 8
    assert range_sum_2d(p2d, 2, 1, 4, 3) == 8, "range_sum_2d submatrix"
    # Sum of entire matrix
    total = sum(sum(row) for row in matrix)
    assert range_sum_2d(p2d, 0, 0, 4, 4) == total, "range_sum_2d full matrix"

    print("✅ Template 3 (Prefix Sum) — all assertions passed")

    # ── Template 4: Set for Existence ────────────────────────

    # contains_duplicate
    assert contains_duplicate([1, 2, 3, 1]) is True,  "contains_duplicate True"
    assert contains_duplicate([1, 2, 3, 4]) is False, "contains_duplicate False"
    assert contains_duplicate([]) is False,            "contains_duplicate empty"

    # longest_consecutive_sequence
    assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4, "longest_consecutive basic"
    assert longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9, "longest_consecutive long"
    assert longest_consecutive_sequence([]) == 0, "longest_consecutive empty"

    # first_missing_positive
    assert first_missing_positive([1, 2, 0])       == 3, "first_missing_positive [1,2,0]"
    assert first_missing_positive([3, 4, -1, 1])   == 2, "first_missing_positive [3,4,-1,1]"
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1, "first_missing_positive no 1"
    assert first_missing_positive([1])             == 2, "first_missing_positive single 1"
    assert first_missing_positive([2])             == 1, "first_missing_positive single 2"

    print("✅ Template 4 (Set for Existence) — all assertions passed")

    print()
    print("🎉 All arrays & hashing templates passed!")
