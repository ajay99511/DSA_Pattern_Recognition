"""Sliding Window — Reusable Templates"""
from typing import List
from collections import Counter, defaultdict


# ============================================================
# TEMPLATE 1: Fixed Window
# ============================================================
def max_sum_subarray_k(nums: List[int], k: int) -> int:
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum


# ============================================================
# TEMPLATE 2: Variable Window — Longest Valid
# ============================================================
# Pattern: Expand right always. Shrink left when invalid.
# Answer = max(right - left + 1)

def length_of_longest_substring(s: str) -> int:
    """LC #3 — Longest substring without repeating characters."""
    char_set = set()
    left = max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len


def character_replacement(s: str, k: int) -> int:
    """LC #424 — Longest Repeating Character Replacement.
    Window valid when: (window_size - max_freq) <= k."""
    freq = defaultdict(int)
    left = max_freq = max_len = 0
    for right in range(len(s)):
        freq[s[right]] += 1
        max_freq = max(max_freq, freq[s[right]])
        while (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


# ============================================================
# TEMPLATE 3: Variable Window — Shortest/Minimum Valid
# ============================================================
# Pattern: Expand right to find valid. Shrink left to minimize.
# Answer = min(right - left + 1) when valid

def min_window_substring(s: str, t: str) -> str:
    """LC #76 — Minimum Window Substring."""
    if not t or not s: return ""
    need = Counter(t)
    missing = len(t)
    left = start = 0
    min_len = float('inf')
    
    for right, char in enumerate(s):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        
        while missing == 0:  # Valid window found
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    
    return s[start:start + min_len] if min_len != float('inf') else ""


# ============================================================
# TEMPLATE 4: Fixed Window with Frequency Match
# ============================================================

def find_anagrams(s: str, p: str) -> List[int]:
    """LC #438 — Find All Anagrams in String."""
    if len(p) > len(s): return []
    p_count = Counter(p)
    s_count = Counter(s[:len(p)])
    result = []
    if s_count == p_count: result.append(0)
    
    for i in range(len(p), len(s)):
        s_count[s[i]] += 1               # Add new char
        old = s[i - len(p)]
        s_count[old] -= 1                 # Remove old char
        if s_count[old] == 0: del s_count[old]
        if s_count == p_count:
            result.append(i - len(p) + 1)
    return result


# ============================================================
# TEMPLATE 5: Sliding Window Maximum (Monotonic Deque)
# ============================================================
from collections import deque

def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """LC #239 — O(N) using monotonic decreasing deque."""
    dq = deque()  # Stores indices, values are decreasing
    result = []
    for i in range(len(nums)):
        # Remove elements outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove smaller elements (they'll never be the max)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


if __name__ == "__main__":
    assert max_sum_subarray_k([1,4,2,10,2,3,1,0,20], 4) == 24
    assert length_of_longest_substring("abcabcbb") == 3
    assert character_replacement("AABABBA", 1) == 4
    assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"
    assert find_anagrams("cbaebabacd", "abc") == [0, 6]
    assert max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    print("✅ All sliding window templates passed!")
