"""
## Problem: Minimum Window Substring (LC #76)
- **Pattern**: Arrays & Hashing - Sliding Window + Frequency Map
- **Difficulty**: Hard
- **Key Insight**: Use a sliding window with two frequency maps (need vs. have); expand the right pointer to include required characters, then shrink the left pointer to minimize the window while maintaining validity — track "formed" count to check validity in O(1).
- **Recognition Signal**: "minimum window containing all characters of t" / "smallest substring with all required chars" → sliding window + frequency map
- **Complexity**: Time O(|s| + |t|), Space O(|s| + |t|)
- **My Confidence**: 🔴
- **Review Dates**: [date1] → [date2] → [date3]

## Bridge Note
This problem bridges Arrays & Hashing → Sliding Window (Module 03).
The hash map tracks character frequencies; the sliding window manages the window boundaries.
"""

# STEP-BY-STEP APPROACH:
# 1. Build need = Counter(t): required character frequencies.
# 2. Initialize window = {} (current window frequencies), have = 0, required = len(need).
#    'have' counts how many distinct characters in the window meet their required frequency.
#    'required' is the number of distinct characters we need to satisfy.
# 3. Expand right pointer r:
#    a. Add s[r] to window.
#    b. If window[s[r]] == need[s[r]], increment have (this character is now satisfied).
# 4. While have == required (window is valid):
#    a. Update result if current window is smaller.
#    b. Shrink from left: remove s[l] from window.
#       If window[s[l]] < need[s[l]], decrement have (character no longer satisfied).
#    c. Advance l.
# 5. Return the minimum window found, or "" if none.

# SOLUTION:
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)               # Required character frequencies
        required = len(need)            # Number of distinct characters we must satisfy

        window = {}                     # Current window character frequencies
        have = 0                        # Count of distinct chars currently satisfied

        result = ""                     # Best window found so far
        result_len = float("inf")       # Length of best window (minimize this)
        l = 0                           # Left pointer

        for r in range(len(s)):
            # Expand window to include s[r]
            char = s[r]
            window[char] = window.get(char, 0) + 1

            # Check if this character's frequency now meets the requirement
            if char in need and window[char] == need[char]:
                have += 1               # One more distinct character is satisfied

            # Shrink window from left while all requirements are met
            while have == required:
                # Update result if this window is smaller
                window_size = r - l + 1
                if window_size < result_len:
                    result_len = window_size
                    result = s[l : r + 1]

                # Remove leftmost character from window
                left_char = s[l]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1           # This character is no longer satisfied

                l += 1                  # Shrink window from left

        return result


# TEST CASES:
if __name__ == "__main__":
    s = Solution()

    # LeetCode example 1
    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC", "LC example 1"

    # LeetCode example 2: s == t
    assert s.minWindow("a", "a") == "a", "s equals t"

    # LeetCode example 3: impossible
    assert s.minWindow("a", "aa") == "", "impossible: need 2 a's but only 1"

    # t is longer than s
    assert s.minWindow("ab", "abc") == "", "t longer than s"

    # Entire s is the answer
    assert s.minWindow("abc", "abc") == "abc", "entire string"

    # Duplicate characters in t
    assert s.minWindow("aaflslflsldkalskaaa", "aaa") == "aaa", "need 3 a's"

    # Single character
    assert s.minWindow("a", "b") == "", "no match"

    # Window at the start
    assert s.minWindow("ABCDEF", "ABC") == "ABC", "window at start"

    # Window at the end
    assert s.minWindow("DEFABC", "ABC") == "ABC", "window at end"

    print("✅ All tests passed!")
