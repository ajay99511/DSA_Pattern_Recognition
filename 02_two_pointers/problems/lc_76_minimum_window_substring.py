"""
## Problem: Minimum Window Substring (LC #76)
- **Pattern**: Two Pointers - Same Direction (Sliding Window variant)
- **Difficulty**: Hard
- **Key Insight**: Expand the right pointer until the window contains all required characters, then contract the left pointer to minimize the window — track "formed" count to know when the window is valid in O(1).
- **Recognition Signal**: "minimum window containing all characters of t" / "substring" → same-direction two pointers (sliding window); use a frequency map + formed counter to check validity in O(1)
- **Complexity**: Time O(|S| + |T|), Space O(|S| + |T|)
- **My Confidence**: 🔴
- **Review Dates**: [date1] → [date2] → [date3]
"""

# Problem: Given strings s and t, return the minimum window substring of s that
# contains every character in t (including duplicates). Return "" if no such
# window exists.

# STEP-BY-STEP APPROACH:
# 1. Build need: frequency map of characters required from t.
# 2. formed = 0 (how many unique chars in t are satisfied at required frequency).
# 3. required = number of unique chars in t.
# 4. left = 0, window = {} (current window frequency map).
# 5. Expand right pointer across s:
#    a. Add s[right] to window.
#    b. If window[s[right]] == need[s[right]] → formed++.
#    c. While formed == required (window is valid):
#       - Update best answer if current window is smaller.
#       - Remove s[left] from window; if window[s[left]] < need[s[left]] → formed--.
#       - left++.
# 6. Return best answer or "".

# NOTE: The "formed" counter is the key optimization — it lets us check
# window validity in O(1) instead of scanning the entire frequency map
# every time. We only increment/decrement it at exact threshold crossings.

from collections import Counter


def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""

    need     = Counter(t)                   # WHY: frequency of each char required from t
    required = len(need)                    # WHY: number of unique chars we must satisfy
    window   = {}                           # WHY: frequency of chars in the current window
    formed   = 0                            # WHY: unique chars currently satisfied at required frequency

    left = 0
    best_len   = float("inf")
    best_left  = 0

    for right in range(len(s)):
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1  # WHY: expand window to include s[right]

        # WHY: check if this char's frequency just hit the required threshold
        if ch in need and window[ch] == need[ch]:
            formed += 1

        # WHY: contract from the left while the window is valid
        while formed == required and left <= right:
            # Update best answer if this window is smaller
            if right - left + 1 < best_len:
                best_len  = right - left + 1
                best_left = left

            left_ch = s[left]
            window[left_ch] -= 1            # WHY: remove leftmost char from window
            # WHY: check if removing this char breaks the required frequency
            if left_ch in need and window[left_ch] < need[left_ch]:
                formed -= 1
            left += 1                       # WHY: shrink window from the left

    return "" if best_len == float("inf") else s[best_left: best_left + best_len]


# TEST CASES:
if __name__ == "__main__":
    # Classic example
    assert min_window("ADOBECODEBANC", "ABC") == "BANC",  "classic: BANC"

    # t is a single character
    assert min_window("a", "a") == "a",                   "single char match"

    # No valid window
    assert min_window("a", "b") == "",                    "no valid window"

    # t has duplicate characters
    assert min_window("aa", "aa") == "aa",                "duplicate chars in t"

    # Entire s is the answer
    assert min_window("abc", "abc") == "abc",             "entire string is window"

    # t longer than s
    assert min_window("ab", "abc") == "",                 "t longer than s"

    print("✅ All tests passed!")
