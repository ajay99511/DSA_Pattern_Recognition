"""
## Problem: Valid Anagram (LC #242)
- **Pattern**: Arrays & Hashing - Frequency Counting
- **Difficulty**: Easy
- **Key Insight**: Two strings are anagrams iff they have identical character frequency maps; Counter comparison is O(N) vs O(N log N) for sorting.
- **Recognition Signal**: "anagram" / "same characters different order" → frequency map / Counter comparison
- **Complexity**: Time O(N), Space O(1) — at most 26 lowercase letters in the map
- **My Confidence**: 🟢
- **Review Dates**: [date1] → [date2] → [date3]
"""

# STEP-BY-STEP APPROACH:
# 1. Early exit: if len(s) != len(t), they can't be anagrams.
# 2. Build a frequency map for s using Counter (or a 26-element array).
# 3. Build a frequency map for t.
# 4. Compare the two maps — equal maps mean same characters with same counts.
# 5. Return True if equal, False otherwise.

# SOLUTION:
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):           # Different lengths → impossible to be anagrams
            return False

        return Counter(s) == Counter(t)  # Counter builds {char: count}; equality is O(alphabet size)

    # --- Alternative: manual count array (O(1) space, no imports) ---
    def isAnagram_manual(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26               # One slot per lowercase letter
        for c in s:
            count[ord(c) - ord('a')] += 1   # Increment for s
        for c in t:
            count[ord(c) - ord('a')] -= 1   # Decrement for t

        return all(x == 0 for x in count)   # All zeros → perfectly balanced


# TEST CASES:
if __name__ == "__main__":
    s = Solution()

    # Classic anagram
    assert s.isAnagram("anagram", "nagaram") == True,  "classic anagram"

    # Not an anagram
    assert s.isAnagram("rat", "car") == False,         "not an anagram"

    # Different lengths
    assert s.isAnagram("a", "ab") == False,            "different lengths"

    # Single character match
    assert s.isAnagram("a", "a") == True,              "single char match"

    # Single character mismatch
    assert s.isAnagram("a", "b") == False,             "single char mismatch"

    # Empty strings
    assert s.isAnagram("", "") == True,                "both empty"

    # Same letters different counts
    assert s.isAnagram("aab", "bba") == False,         "same letters different counts"

    # Manual version
    assert s.isAnagram_manual("anagram", "nagaram") == True
    assert s.isAnagram_manual("rat", "car") == False

    print("✅ All tests passed!")
