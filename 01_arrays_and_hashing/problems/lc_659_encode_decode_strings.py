"""
## Problem: Encode and Decode Strings (LC #659 / LC #271 equivalent)
- **Pattern**: Arrays & Hashing - Length-Prefix Encoding
- **Difficulty**: Medium
- **Key Insight**: Prefix each word with its length and a delimiter (e.g., "4#word") so the decoder can read the exact number of characters without ambiguity, even if words contain the delimiter character.
- **Recognition Signal**: "encode list of strings to single string" / "decode back to original list" → length-prefix encoding
- **Complexity**: Time O(N) encode, O(N) decode; Space O(N) for the encoded string
- **My Confidence**: 🟡
- **Review Dates**: [date1] → [date2] → [date3]
"""

# STEP-BY-STEP APPROACH:
#
# ENCODE:
# 1. For each word, prepend len(word) + "#" + word.
# 2. Concatenate all encoded words into one string.
#    Example: ["hello", "world"] → "5#hello5#world"
#
# DECODE:
# 1. Start at index i = 0.
# 2. Find the next "#" starting from i.
# 3. Read the length = int(encoded[i:j]).
# 4. The word is encoded[j+1 : j+1+length].
# 5. Advance i to j+1+length and repeat.
#
# WHY length-prefix: simple delimiters (like comma or space) fail if words contain them.
# Length-prefix is unambiguous regardless of word content.

# SOLUTION:
class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encode a list of strings to a single string."""
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word  # "4#word" format
        return encoded

    def decode(self, s: str) -> list[str]:
        """Decode a single string back to the original list of strings."""
        result = []
        i = 0

        while i < len(s):
            j = s.index("#", i)             # Find the delimiter '#' starting from i
            length = int(s[i:j])            # Read the length prefix
            word = s[j + 1 : j + 1 + length]  # Extract exactly 'length' characters
            result.append(word)
            i = j + 1 + length              # Advance past this encoded word

        return result


# TEST CASES:
if __name__ == "__main__":
    codec = Codec()

    # Classic example
    words = ["hello", "world"]
    assert codec.decode(codec.encode(words)) == words, "classic"

    # Words containing the delimiter '#'
    words = ["a#b", "c#d#e"]
    assert codec.decode(codec.encode(words)) == words, "words with # delimiter"

    # Empty string in list
    words = ["", "hello", ""]
    assert codec.decode(codec.encode(words)) == words, "empty strings"

    # Single word
    words = ["onlyone"]
    assert codec.decode(codec.encode(words)) == words, "single word"

    # Empty list
    words = []
    assert codec.decode(codec.encode(words)) == words, "empty list"

    # Words with spaces
    words = ["hello world", "foo bar"]
    assert codec.decode(codec.encode(words)) == words, "words with spaces"

    # Long word
    words = ["a" * 1000]
    assert codec.decode(codec.encode(words)) == words, "long word"

    # Numbers as strings
    words = ["123", "456", "789"]
    assert codec.decode(codec.encode(words)) == words, "numeric strings"

    print("✅ All tests passed!")
