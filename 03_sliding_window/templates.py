"""
Sliding Window — Reusable Templates
=====================================
Three production-quality O(N) templates for FAANG interview preparation.

  1. FIXED WINDOW         — constant-size window; numeric (max sum of size k)
                            + frequency variant (anagram / permutation matching)
  2. VARIABLE WINDOW      — expand right always; shrink left when constraint
  LONGEST                   violated (at most k distinct, no repeating chars,
                            at most k zeros / replacements)
  3. VARIABLE WINDOW      — expand right to find a valid window; shrink left
  SHORTEST                  to minimize it (min window substring, min subarray sum)

Each template includes:
  • Recognition signals  — problem keywords that trigger this template
  • Annotated skeleton   — every key line explained with WHY, not just WHAT
  • Concrete examples    — 2-3 worked LeetCode problems with traces
  • Complexity           — Time O(N) and Space annotations
  • Runnable assertions  — normal, edge, and corner cases verified in __main__

Run with:  python templates.py
"""

from typing import List
from collections import Counter, defaultdict


# ============================================================
# TEMPLATE 1: FIXED WINDOW
# ============================================================
#
# RECOGNITION SIGNALS
# -------------------
#   "subarray / substring of size K"
#   "maximum / minimum / average of every window of size K"
#   "permutation in string" / "anagram in string"
#   "find all starting indices where p is an anagram of s"
#   Any problem where the window size is given and never changes
#
# CORE IDEA
# ---------
#   Build the first window of size k from scratch (O(k)).
#   Then slide one position at a time: add nums[i] (right edge enters),
#   remove nums[i - k] (left edge exits).  Each slide is O(1).
#   Total: O(N) instead of O(N·K) brute force.
#
#   Visual — nums = [2, 1, 5, 1, 3, 2], k = 3:
#
#     Step 0:  [2  1  5] 1  3  2   window_sum = 8
#               L     R
#     Step 1:   2 [1  5  1] 3  2   window_sum = 8 - 2 + 1 = 7
#                  L     R
#     Step 2:   2  1 [5  1  3] 2   window_sum = 7 - 1 + 3 = 9  ← max
#                     L     R
#     Step 3:   2  1  5 [1  3  2]  window_sum = 9 - 5 + 2 = 6
#                        L     R
#     Answer: 9
#
# SKELETON
# --------
#   window_sum = sum(nums[:k])          # seed the first window
#   result = window_sum
#   for i in range(k, len(nums)):
#       window_sum += nums[i]           # right edge enters
#       window_sum -= nums[i - k]       # left edge exits (exactly k behind)
#       result = max(result, window_sum)
#   return result
#
# COMPLEXITY: Time O(N)  |  Space O(1) numeric; O(Σ) frequency variant
# ============================================================


def max_sum_subarray_k(nums: List[int], k: int) -> int:
    """
    LC #643 variant — Maximum sum of any contiguous subarray of size k.

    WHY fixed window: the window size is constant (k), so we never need
    to shrink.  We just slide: one element enters from the right, one
    leaves from the left.  Each slide is O(1) → O(N) total.

    Trace: nums = [2, 1, 5, 1, 3, 2], k = 3
      Seed:   window_sum = 2+1+5 = 8,  result = 8
      i=3:    +1 -2 → 7,  result = 8
      i=4:    +3 -1 → 9,  result = 9  ← max
      i=5:    +2 -5 → 6,  result = 9
      Return 9  ✓

    Complexity: Time O(N) — one pass after O(k) seed.
                Space O(1) — only two scalar variables.
    """
    if not nums or k > len(nums):        # WHY guard: k larger than array has no valid window
        return 0

    window_sum = sum(nums[:k])           # WHY seed: build the first window from scratch; O(k)
    result = window_sum                  # WHY: first window is a valid candidate for the answer

    for i in range(k, len(nums)):
        window_sum += nums[i]            # WHY: right edge enters — new element joins the window
        window_sum -= nums[i - k]        # WHY: left edge exits — nums[i-k] is exactly k behind nums[i]
                                         #      i.e., the element that was at the left of the previous window
        result = max(result, window_sum) # WHY max: track the best window seen so far
                                         #      change to min() for minimum-sum problems

    return result


def permutation_in_string(s1: str, s2: str) -> bool:
    """
    LC #567 — Permutation in String.
    Return True if any permutation of s1 is a substring of s2.

    WHY fixed window + frequency match: a permutation has the same
    character frequencies as the original.  A fixed window of len(s1)
    slides across s2; at each position we check if the window's
    frequency map matches s1's.  Window size never changes → fixed window.

    WHY track 'matches' count instead of full Counter comparison:
    Counter comparison is O(Σ) per step.  Instead, maintain an integer
    'matches' = number of characters whose frequency is satisfied.
    When matches == len(need), the window is a valid permutation.
    This keeps each slide at O(1).

    Trace: s1 = "ab", s2 = "eidbaooo"
      need = {'a':1, 'b':1},  matches = 0
      Seed window "ei": window={'e':1,'i':1}, matches=0
      Slide i=2 ('d'): add 'd', remove 'e' → window={'i':1,'d':1}, matches=0
      Slide i=3 ('b'): add 'b' → need['b'] satisfied → matches=1
                        remove 'i' → matches=1
      Slide i=4 ('a'): add 'a' → need['a'] satisfied → matches=2
                        remove 'd' → matches=2  → return True  ✓

    Complexity: Time O(N) where N = len(s2).  Space O(Σ) = O(26).
    """
    k = len(s1)
    if k > len(s2):                      # WHY: s1 can't fit inside s2 at all
        return False

    need   = Counter(s1)                 # WHY: target frequency map for s1
    window = Counter(s2[:k])             # WHY: frequency map of the first window (seed)
    # WHY matches: count how many distinct chars have their frequency satisfied
    matches = sum(1 for c in need if window[c] == need[c])

    if matches == len(need):             # WHY: check the very first window before sliding
        return True

    for i in range(k, len(s2)):
        incoming = s2[i]                 # WHY: character entering the right edge of the window
        outgoing = s2[i - k]             # WHY: character leaving the left edge (exactly k behind)

        # ── Add incoming character ────────────────────────────────────────
        window[incoming] += 1
        if incoming in need:
            if window[incoming] == need[incoming]:
                matches += 1             # WHY: this char just became fully satisfied
            elif window[incoming] == need[incoming] + 1:
                matches -= 1             # WHY: we now have one too many — no longer satisfied

        # ── Remove outgoing character ─────────────────────────────────────
        window[outgoing] -= 1
        if outgoing in need:
            if window[outgoing] == need[outgoing]:
                matches += 1             # WHY: removing excess brought us back to exact count
            elif window[outgoing] == need[outgoing] - 1:
                matches -= 1             # WHY: we just lost a needed character

        if matches == len(need):         # WHY: all characters satisfied → valid permutation window
            return True

    return False


def find_anagrams(s: str, p: str) -> List[int]:
    """
    LC #438 — Find All Anagrams in a String.
    Return all starting indices in s where an anagram of p begins.

    WHY same fixed-window approach as LC #567: an anagram is just a
    permutation.  The only difference is we collect ALL valid starting
    indices instead of returning True on the first match.

    WHY clean up zero-count keys: Counter equality checks all keys.
    Leaving zero-count keys in window would cause false mismatches
    (e.g., window={'a':1, 'b':0} != p_count={'a':1}).

    Trace: s = "cbaebabacd", p = "abc"
      p_count = {'a':1,'b':1,'c':1}
      Seed "cba": window={'c':1,'b':1,'a':1} == p_count → append 0
      i=3 ('e'): add 'e', remove 'c' → window={'b':1,'a':1,'e':1} ≠ p_count
      i=4 ('b'): add 'b', remove 'b' → window={'b':1,'a':1,'e':1} ≠ p_count
      i=5 ('a'): add 'a', remove 'a' → window={'b':1,'a':1,'e':1} ≠ p_count
      i=6 ('b'): add 'b', remove 'e' → window={'b':2,'a':1} ≠ p_count
      i=7 ('a'): add 'a', remove 'b' → window={'b':1,'a':2} ≠ p_count
      i=8 ('c'): add 'c', remove 'a' → window={'b':1,'a':1,'c':1} == p_count → append 6
      i=9 ('d'): add 'd', remove 'b' → window={'a':1,'c':1,'d':1} ≠ p_count
      Return [0, 6]  ✓

    Complexity: Time O(N) where N = len(s).  Space O(Σ) = O(26).
    """
    k = len(p)
    if k > len(s):                       # WHY: p can't fit inside s
        return []

    p_count = Counter(p)                 # WHY: target frequency map
    window  = Counter(s[:k])             # WHY: seed the first window
    result  = []

    if window == p_count:                # WHY: check the first window before the loop
        result.append(0)

    for i in range(k, len(s)):
        # ── Slide: add incoming, remove outgoing ──────────────────────────
        window[s[i]] += 1                # WHY: right edge enters

        outgoing = s[i - k]              # WHY: the character that just left the left edge
        window[outgoing] -= 1
        if window[outgoing] == 0:
            del window[outgoing]         # WHY: remove zero-count keys so Counter equality works

        if window == p_count:            # WHY O(26): comparing two Counters over a 26-char alphabet
            result.append(i - k + 1)    # WHY i-k+1: left edge of the current window

    return result


# ============================================================
# TEMPLATE 2: VARIABLE WINDOW — LONGEST VALID
# ============================================================
#
# RECOGNITION SIGNALS
# -------------------
#   "longest substring / subarray"
#   "at most K distinct characters"
#   "longest substring without repeating characters"
#   "at most K replacements" / "at most K zeros"
#   "longest subarray with sum ≤ target"
#   Any problem asking for the MAXIMUM window satisfying a constraint
#
# CORE IDEA
# ---------
#   right always advances (we never skip an element).
#   left only advances when the constraint is violated.
#   After the while loop, [left..right] is guaranteed valid.
#   max_len = max(max_len, right - left + 1) after every right step.
#
#   The key insight: right moves N times total; left moves at most N
#   times total (it never goes backward) → O(N) amortized.
#
#   Visual — s = "abcabcbb", find longest without repeating chars:
#
#     right → a  b  c  a  b  c  b  b
#     left=0  [a]                        len=1
#             [a  b]                     len=2
#             [a  b  c]                  len=3  ← max
#             [a  b  c  a] ← 'a' repeats!
#                [b  c  a]  shrink: remove 'a'
#                [b  c  a  b] ← 'b' repeats!
#                   [c  a  b]  shrink: remove 'b'
#                   ...
#     Answer: 3
#
# SKELETON
# --------
#   freq = defaultdict(int)   # or a set, or a counter
#   left = 0
#   max_len = 0
#   for right in range(len(s)):
#       freq[s[right]] += 1              # expand: add right element
#       while <constraint violated>:     # shrink until valid again
#           freq[s[left]] -= 1
#           if freq[s[left]] == 0: del freq[s[left]]
#           left += 1
#       max_len = max(max_len, right - left + 1)
#   return max_len
#
# CUSTOMIZE THE while CONDITION:
#   "at most k distinct":       while len(freq) > k
#   "no repeating chars":       while freq[s[right]] > 1
#   "at most k replacements":   while (right-left+1) - max(freq.values()) > k
#   "at most k zeros":          while zeros_in_window > k
#
# COMPLEXITY: Time O(N)  |  Space O(Σ) for the frequency map
# ============================================================


def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    LC #340 — Longest Substring with At Most K Distinct Characters.
    Generic variable-window-longest template instantiation.

    WHY variable window: the window can grow as long as we have ≤ k
    distinct characters.  The moment we exceed k distinct chars, we
    shrink from the left until we're back to k.  We never skip a
    right-side element, so right advances N times total.

    WHY delete zero-count keys: len(freq) counts distinct characters.
    Leaving zero-count keys would inflate len(freq) and cause premature
    shrinking.

    Trace: s = "eceba", k = 2
      right=0 ('e'): freq={'e':1}, len=1 ≤ 2 → max_len=1
      right=1 ('c'): freq={'e':1,'c':1}, len=2 ≤ 2 → max_len=2
      right=2 ('e'): freq={'e':2,'c':1}, len=2 ≤ 2 → max_len=3
      right=3 ('b'): freq={'e':2,'c':1,'b':1}, len=3 > 2 → shrink:
        remove s[0]='e': freq={'e':1,'c':1,'b':1}, left=1, len=3 > 2 → shrink:
        remove s[1]='c': freq={'e':1,'b':1}, left=2, len=2 ≤ 2 → max_len=3
      right=4 ('a'): freq={'e':1,'b':1,'a':1}, len=3 > 2 → shrink:
        remove s[2]='e': freq={'b':1,'a':1}, left=3, len=2 ≤ 2 → max_len=3
      Return 3  ("ece")  ✓

    Complexity: Time O(N).  Space O(k) — at most k+1 keys before shrink.
    """
    freq  = defaultdict(int)             # WHY: track character frequencies in the current window
    left  = 0
    max_len = 0

    for right in range(len(s)):
        freq[s[right]] += 1              # WHY: expand — add the right-edge character

        while len(freq) > k:             # WHY while (not if): one shrink step may not restore validity
            freq[s[left]] -= 1           # WHY: remove the left-edge character from the window
            if freq[s[left]] == 0:
                del freq[s[left]]        # WHY: remove zero-count key so len(freq) stays accurate
            left += 1                    # WHY: shrink the window from the left

        # WHY here: after the while loop, [left..right] is guaranteed valid
        max_len = max(max_len, right - left + 1)

    return max_len


def length_of_longest_substring(s: str) -> int:
    """
    LC #3 — Longest Substring Without Repeating Characters.

    WHY set instead of Counter: we only need to know if a character is
    present (not its count), so a set is simpler and equally efficient.

    WHY shrink with while: when s[right] is already in the set, we must
    remove characters from the left until the duplicate is gone.  This
    may require multiple removals (e.g., "abcda" — when 'a' repeats,
    we remove 'a','b','c' before the window is valid again).

    Trace: s = "abcabcbb"
      right=0 ('a'): seen={}, add 'a' → seen={'a'}, max_len=1
      right=1 ('b'): 'b' not in seen → seen={'a','b'}, max_len=2
      right=2 ('c'): 'c' not in seen → seen={'a','b','c'}, max_len=3
      right=3 ('a'): 'a' in seen → remove s[0]='a', left=1
                     'a' not in seen → add 'a' → seen={'b','c','a'}, max_len=3
      right=4 ('b'): 'b' in seen → remove s[1]='b', left=2
                     'b' not in seen → add 'b' → seen={'c','a','b'}, max_len=3
      right=5 ('c'): 'c' in seen → remove s[2]='c', left=3
                     'c' not in seen → add 'c' → seen={'a','b','c'}, max_len=3
      right=6 ('b'): 'b' in seen → remove s[3]='a', left=4
                     'b' still in seen → remove s[4]='b', left=5
                     'b' not in seen → add 'b' → seen={'c','b'}, max_len=3
      right=7 ('b'): 'b' in seen → remove s[5]='c', left=6
                     'b' still in seen → remove s[6]='b', left=7
                     'b' not in seen → add 'b' → seen={'b'}, max_len=3
      Return 3  ✓

    Complexity: Time O(N) — each character added and removed at most once.
                Space O(min(N, Σ)) — set holds at most Σ distinct chars.
    """
    seen  = set()                        # WHY set: O(1) membership check and removal
    left  = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:          # WHY while: keep shrinking until the duplicate is gone
            seen.remove(s[left])         # WHY: remove the leftmost character from the window
            left += 1                    # WHY: advance left pointer past the removed character

        seen.add(s[right])               # WHY: now s[right] is safe to add (no duplicate)
        max_len = max(max_len, right - left + 1)

    return max_len


def character_replacement(s: str, k: int) -> int:
    """
    LC #424 — Longest Repeating Character Replacement.
    Find the longest substring where you can replace at most k characters
    to make all characters the same.

    WHY the constraint is (window_size - max_freq) <= k:
    In a window of size W, the minimum replacements needed to make all
    characters the same is W minus the count of the most frequent char.
    If that cost exceeds k, the window is invalid.

    WHY max_freq never needs to decrease:
    We only care about windows LARGER than the current best.  If max_freq
    doesn't increase, the window can't grow beyond its current size, so
    we just slide (left advances with right).  We never need to shrink
    below the current best length.  This is a subtle but important
    optimization — max_freq is a "high-water mark", not the true current max.

    Trace: s = "AABABBA", k = 1
      right=0 ('A'): freq={'A':1}, max_freq=1, window=1, cost=0 ≤ 1 → max_len=1
      right=1 ('A'): freq={'A':2}, max_freq=2, window=2, cost=0 ≤ 1 → max_len=2
      right=2 ('B'): freq={'A':2,'B':1}, max_freq=2, window=3, cost=1 ≤ 1 → max_len=3
      right=3 ('A'): freq={'A':3,'B':1}, max_freq=3, window=4, cost=1 ≤ 1 → max_len=4
      right=4 ('B'): freq={'A':3,'B':2}, max_freq=3, window=5, cost=2 > 1 → shrink:
        remove s[0]='A': freq={'A':2,'B':2}, left=1, window=4, cost=2 > 1 → shrink:
        remove s[1]='A': freq={'A':1,'B':2}, left=2, window=3, cost=1 ≤ 1 → max_len=4
      right=5 ('B'): freq={'A':1,'B':3}, max_freq=3, window=4, cost=1 ≤ 1 → max_len=4
      right=6 ('A'): freq={'A':2,'B':3}, max_freq=3, window=5, cost=2 > 1 → shrink:
        remove s[2]='B': freq={'A':2,'B':2}, left=3, window=4, cost=2 > 1 → shrink:
        remove s[3]='A': freq={'A':1,'B':2}, left=4, window=3, cost=2 > 1 → shrink:
        remove s[4]='B': freq={'A':1,'B':1}, left=5, window=2, cost=1 ≤ 1 → max_len=4
      Return 4  ("AABA" with 1 replacement → "AAAA")  ✓

    Complexity: Time O(N).  Space O(Σ) = O(26).
    """
    freq     = defaultdict(int)          # WHY: track character frequencies in the window
    left     = 0
    max_freq = 0                         # WHY: high-water mark of the most frequent char count
    max_len  = 0

    for right in range(len(s)):
        freq[s[right]] += 1              # WHY: expand — add the right-edge character
        max_freq = max(max_freq, freq[s[right]])  # WHY: update the high-water mark

        # WHY while: if cost > k, window is invalid; shrink until valid
        # cost = (right - left + 1) - max_freq = replacements needed
        while (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1           # WHY: remove the left-edge character
            left += 1                    # WHY: shrink the window
            # WHY NOT update max_freq here: we only care about windows larger
            # than the current best; max_freq as a high-water mark is sufficient

        max_len = max(max_len, right - left + 1)

    return max_len


def longest_ones(nums: List[int], k: int) -> int:
    """
    LC #1004 — Max Consecutive Ones III.
    Find the longest subarray of 1s after flipping at most k zeros.

    WHY variable window: we have a "budget" of k zeros we can include.
    Expand right freely; when zeros_in_window exceeds k, shrink left
    until we're back within budget.

    Trace: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
      Expand until zeros_in_window > 2:
        right=0..2: all 1s, zeros=0, max_len=3
        right=3: 0 → zeros=1, max_len=4
        right=4: 0 → zeros=2, max_len=5
        right=5: 0 → zeros=3 > 2 → shrink:
          left=0 (1): zeros still 3, left=1
          left=1 (1): zeros still 3, left=2
          left=2 (1): zeros still 3, left=3
          left=3 (0): zeros=2, left=4 → window=[4..5], valid
        right=6..9: all 1s, zeros=2, window grows to [4..9], max_len=6
        right=10: 0 → zeros=3 > 2 → shrink:
          left=4 (0): zeros=2, left=5 → window=[5..10], max_len=6
      Return 6  ✓

    Complexity: Time O(N).  Space O(1) — only a counter variable.
    """
    left            = 0
    zeros_in_window = 0                  # WHY: track how many zeros are in the current window
    max_len         = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros_in_window += 1         # WHY: count the zero we just included in the window

        while zeros_in_window > k:       # WHY while: keep shrinking until within budget
            if nums[left] == 0:
                zeros_in_window -= 1     # WHY: we're removing a zero from the window
            left += 1                    # WHY: shrink from the left

        max_len = max(max_len, right - left + 1)

    return max_len


# ============================================================
# TEMPLATE 3: VARIABLE WINDOW — SHORTEST VALID
# ============================================================
#
# RECOGNITION SIGNALS
# -------------------
#   "minimum window substring"
#   "smallest subarray with sum ≥ target"
#   "shortest subarray containing all characters of t"
#   "minimum length subarray satisfying a condition"
#   Any problem asking for the MINIMUM window that satisfies a constraint
#
# CORE IDEA
# ---------
#   This is the INVERSE of the longest-window template:
#     • Expand right to FIND a valid window (make it valid)
#     • Shrink left to MINIMIZE the window (keep it valid as long as possible)
#
#   The inner while loop fires only when the window IS valid.
#   We record the answer INSIDE the shrink loop (every valid window is a candidate).
#   We stop shrinking when the window becomes invalid again.
#
#   Visual — s = "ADOBECODEBANC", t = "ABC":
#
#     Expand right until window contains A, B, C:
#       right=0..5: "ADOBEC" → contains A,B,C → valid!
#     Shrink left while still valid:
#       remove 'A' → "DOBEC" → missing A → invalid, stop
#       best = "ADOBEC" (len 6)
#     Continue expanding right:
#       right=6..9: "DOBECODEBA" → contains A,B,C → valid!
#     Shrink left:
#       remove 'D' → "OBECODEBA" → still valid, best = len 9 (no improvement)
#       remove 'O' → "BECODEBA" → still valid
#       remove 'B' → "ECODEBA" → still valid
#       remove 'E' → "CODEBA" → still valid
#       remove 'C' → "ODEBA" → missing C → invalid, stop
#       best = "CODEBA" (len 6, no improvement)
#     Continue expanding right:
#       right=10: "ODEBANC" → contains A,B,C → valid!
#     Shrink left:
#       remove 'O' → "DEBANC" → still valid, best = len 6 (no improvement)
#       remove 'D' → "EBANC" → still valid, best = "EBANC" (len 5, no improvement)
#       remove 'E' → "BANC" → still valid, best = "BANC" (len 4)  ← new best!
#       remove 'B' → "ANC" → missing B → invalid, stop
#     Answer: "BANC"
#
# SKELETON
# --------
#   need = Counter(t)
#   missing = len(t)          # total characters still needed
#   left = best_start = 0
#   best_len = float('inf')
#   for right, char in enumerate(s):
#       if need[char] > 0: missing -= 1   # this char was needed
#       need[char] -= 1                    # can go negative (excess)
#       while missing == 0:               # window is valid: try to shrink
#           if right - left + 1 < best_len:
#               best_len = right - left + 1
#               best_start = left
#           need[s[left]] += 1            # "un-add" the left char
#           if need[s[left]] > 0: missing += 1  # we lost a needed char
#           left += 1
#   return s[best_start : best_start + best_len]
#
# KEY TRICK: the 'missing' counter
#   missing starts at len(t) and decrements to 0 when the window is valid.
#   need[char] can go negative (we have excess copies of char).
#   Only need[char] > 0 means we actually need that character.
#   This lets us track validity in O(1) per step instead of O(|t|).
#
# COMPLEXITY: Time O(N + |t|)  |  Space O(|t| + Σ)
# ============================================================


def min_window_substring(s: str, t: str) -> str:
    """
    LC #76 — Minimum Window Substring.
    Find the shortest substring of s that contains all characters of t.

    WHY 'missing' counter instead of comparing Counters each step:
    Comparing two Counters is O(|t|) per step → O(N·|t|) total.
    The 'missing' integer tracks validity in O(1) per step.

    WHY need[char] can go negative:
    We may have more copies of a character than t requires.  Negative
    values mean "excess".  Only need[char] > 0 means we still need it.
    This lets us handle duplicate characters in t correctly.

    Trace: s = "ADOBECODEBANC", t = "ABC"
      need = {'A':1, 'B':1, 'C':1},  missing = 3
      right=0 ('A'): need['A']=1>0 → missing=2; need['A']=0
      right=1 ('D'): need['D']=0, not needed; need['D']=-1
      right=2 ('O'): need['O']=-1
      right=3 ('B'): need['B']=1>0 → missing=1; need['B']=0
      right=4 ('E'): need['E']=-1
      right=5 ('C'): need['C']=1>0 → missing=0; need['C']=0
        → missing==0: best=(0,6,"ADOBEC")
        shrink: need['A']+=1=1>0 → missing=1; left=1 → exit while
      right=6..9: expand, missing reaches 0 again at right=9 ('A')
        → missing==0: best stays "ADOBEC" (len 6)
        shrink until invalid...
      right=10 ('N'): need['N']=-1
      right=11 ('C'): need['C']=1>0 → missing=0; need['C']=0
        → missing==0: best="BANC" (len 4)  ← final answer
      Return "BANC"  ✓

    Complexity: Time O(N + |t|) — each pointer moves at most N times.
                Space O(|t| + Σ) — need Counter plus window tracking.
    """
    if not t or not s:                   # WHY: empty inputs have no valid window
        return ""

    need       = Counter(t)              # WHY: required character frequencies
    missing    = len(t)                  # WHY: total characters still needed; 0 means window is valid
    left       = 0
    best_start = 0
    best_len   = float('inf')            # WHY inf: any valid window will be smaller

    for right, char in enumerate(s):
        # ── Expand: add s[right] to the window ────────────────────────────
        if need[char] > 0:               # WHY > 0: this character is still needed (not excess)
            missing -= 1                 # WHY: one fewer character needed to make window valid
        need[char] -= 1                  # WHY: decrement regardless (can go negative = excess)

        # ── Shrink: while window is valid, try to minimize it ─────────────
        while missing == 0:              # WHY while: keep shrinking as long as window stays valid
            if right - left + 1 < best_len:   # WHY: this valid window might be the shortest so far
                best_len   = right - left + 1
                best_start = left        # WHY: record the start of the best window

            need[s[left]] += 1           # WHY: "un-add" the leftmost character from the window
            if need[s[left]] > 0:        # WHY > 0: we actually needed that character
                missing += 1             # WHY: window is now invalid — the while loop will exit
            left += 1                    # WHY: advance left regardless (shrink the window)

    return s[best_start : best_start + best_len] if best_len != float('inf') else ""
