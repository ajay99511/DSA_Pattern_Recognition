"""
## Problem: Valid Palindrome (LC #125)
- **Pattern**: Two Pointers - Opposite Direction
- **Difficulty**: Easy
- **Key Insight**: Converge from both ends, skipping non-alphanumeric characters; a mismatch at any point immediately disproves the palindrome.
- **Recognition Signal**: "reads the same forwards and backwards" / "alphanumeric only" → opposite-direction pointers from both ends
- **Complexity**: Time O(N), Space O(1)
- **My Confidence**: 🟢
- **Review Dates**: [date1] → [date2] → [date3]
"""

# Problem: Given a string s, return True if it is a palindrome after converting
# all uppercase letters to lowercase and removing all non-alphanumeric characters.
# An empty string is considered a palindrome.

# STEP-BY-STEP APPROACH:
# 1. Place left pointer at index 0, right pointer at index len(s)-1.
# 2. While left < right:
#    a. Advance left past any non-alphanumeric character.
#    b. Retreat right past any non-alphanumeric character.
#    c. Compare s[left].lower() with s[right].lower().
#    d. If they differ → return False.
#    e. Otherwise advance both pointers inward.
# 3. If the loop completes without a mismatch → return True.

# NOTE: Skipping non-alphanumeric inside the loop (not via a cleaned copy)
# keeps space O(1) — no extra string allocation needed.


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric from the left
        while left < right and not s[left].isalnum():   # WHY: punctuation/spaces are ignored
            left += 1
        # Skip non-alphanumeric from the right
        while left < right and not s[right].isalnum():  # WHY: same rule from the right end
            right -= 1

        if s[left].lower() != s[right].lower():         # WHY lower(): case-insensitive comparison
            return False                                 # WHY: mismatch → cannot be a palindrome

        left  += 1                                       # WHY: matched pair; move both inward
        right -= 1

    return True                                          # WHY: all pairs matched → it is a palindrome


# TEST CASES:
if __name__ == "__main__":
    # Classic example with spaces and punctuation
    assert is_palindrome("A man, a plan, a canal: Panama") is True,  "classic palindrome"

    # Not a palindrome
    assert is_palindrome("race a car") is False,                      "not a palindrome"

    # Empty string → palindrome by definition
    assert is_palindrome("") is True,                                 "empty string"

    # Only non-alphanumeric characters → treated as empty → palindrome
    assert is_palindrome(".,") is True,                               "only punctuation"

    # Mixed alphanumeric where case matters
    assert is_palindrome("0P") is False,                              "digit vs letter"

    # Single character
    assert is_palindrome("a") is True,                                "single character"

    print("✅ All tests passed!")
