"""
## Problem: Group Anagrams (LC #49)
- **Pattern**: Arrays & Hashing - Canonical Key Grouping
- **Difficulty**: Medium
- **Key Insight**: All anagrams share the same sorted character sequence; use that sorted tuple as a hash map key to group them in one pass.
- **Recognition Signal**: "group strings that are anagrams of each other" → canonical key + defaultdict(list)
- **Complexity**: Time O(N * M log M) where N = number of strings, M = average string length; Space O(N * M)
- **My Confidence**: 🟢
- **Review Dates**: [date1] → [date2] → [date3]
"""

# STEP-BY-STEP APPROACH:
# 1. Create a defaultdict(list) to map canonical_key → [list of anagrams].
# 2. For each string s:
#    a. Compute canonical key = tuple(sorted(s))
#       — sorted() returns a list; wrap in tuple() to make it hashable.
#       — All anagrams produce the same sorted sequence.
#    b. Append s to groups[key].
# 3. Return list(groups.values()) — the grouped anagram lists.

# ALTERNATIVE (O(N*M) time): Use a 26-element count tuple as the key instead of sorting.
# This avoids the O(M log M) sort per string.

# SOLUTION:
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)          # canonical_key → [anagram strings]

        for s in strs:
            key = tuple(sorted(s))          # Sort chars → same key for all anagrams
                                            # tuple() makes it hashable as a dict key
            groups[key].append(s)           # Group this string under its canonical key

        return list(groups.values())        # Return all groups; discard the keys

    # --- Alternative: O(N*M) using character count tuple as key ---
    def groupAnagrams_count_key(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26                # One slot per lowercase letter
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)              # 26-element tuple is hashable; avoids sorting
            groups[key].append(s)

        return list(groups.values())


# TEST CASES:
if __name__ == "__main__":
    s = Solution()

    def normalize(groups):
        """Sort each group and the list of groups for deterministic comparison."""
        return sorted([sorted(g) for g in groups])

    # Classic example
    result = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert normalize(result) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]], "classic"

    # Single string
    assert normalize(s.groupAnagrams(["a"])) == [["a"]], "single string"

    # All same string
    assert normalize(s.groupAnagrams([""])) == [[""]], "empty string"

    # All anagrams of each other
    result = s.groupAnagrams(["abc", "bca", "cab"])
    assert normalize(result) == [["abc", "bca", "cab"]], "all anagrams"

    # No anagrams — each string is its own group
    result = s.groupAnagrams(["abc", "def", "ghi"])
    assert normalize(result) == [["abc"], ["def"], ["ghi"]], "no anagrams"

    # Count-key alternative
    result2 = s.groupAnagrams_count_key(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert normalize(result2) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]], "count key"

    print("✅ All tests passed!")
