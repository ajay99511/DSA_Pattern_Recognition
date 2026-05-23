"""
## Problem: Encode and Decode Strings (LC #271)
- **Pattern**: Arrays & Hashing - Length-Prefix Encoding
- **Difficulty**: Hard
- **Key Insight**: Prefix each string with its byte length and a fixed delimiter (e.g., "4#word") so the decoder can extract exactly the right number of characters without ambiguity — works even when strings contain the delimiter or any special character.
- **Recognition Signal**: "design encode/decode for list of strings" / "serialize/deserialize string list" → length-prefix encoding
- **Complexity**: Time O(N) encode, O(N) decode; Space O(N)
- **My Confidence**: 🟡
- **Review Dates**: [date1] → [date2] → [date3]
"""

# STEP-BY-STEP APPROACH:
#
# ENCODE:
# For each word w: append str(len(w)) + "#" + w to the result.
# The '#' is the delimiter between the length and the content.
# Example: ["lint","code","love","you"] → "4#lint4#code4#love3#you"
#
# DECODE:
# i = 0
# While i < len(s):
#   j = index of '#' starting from i
#   length = int(s[i:j])
#   word = s[j+1 : j+1+length]
#   append word; advance i = j+1+length
#
# WHY this is robust: even if a word contains '#' or digits, the length prefix
# tells us exactly how many characters to read, so we never misparse.
#
# EDGE CASES:
# - Empty string in list: encoded as "0#" — length 0, no characters follow.
# - Empty list: encoded as "" — decoded back to [].
# - Words containing '#': handled correctly because we read by length, not by delimiter.

# SOLUTION:
class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encode a list of strings into a single string using length-prefix format."""
        result = []
        for word in strs:
            result.append(f"{len(word)}#{word}")   # "length#content" for each word
        return "".join(result)

    def decode(self, s: str) -> list[str]:
        """Decode a length-prefix encoded string back to the original list."""
        result = []
        i = 0

        while i < len(s):
            j = s.index("#", i)                    # Find the '#' delimiter from position i
            length = int(s[i:j])                   # Parse the length prefix
            word = s[j + 1 : j + 1 + length]       # Extract exactly 'length' characters
            result.append(word)
            i = j + 1 + length                     # Advance past this encoded entry

        return result


# TEST CASES:
if __name__ == "__main__":
    codec = Codec()

    def roundtrip(words):
        return codec.decode(codec.encode(words))

    # LeetCode example
    assert roundtrip(["lint", "code", "love", "you"]) == ["lint", "code", "love", "you"], "LC example"

    # Words containing '#'
    assert roundtrip(["a#b", "c##d"]) == ["a#b", "c##d"], "words with #"

    # Empty string in list
    assert roundtrip(["", "hello", ""]) == ["", "hello", ""], "empty strings"

    # Empty list
    assert roundtrip([]) == [], "empty list"

    # Single word
    assert roundtrip(["onlyone"]) == ["onlyone"], "single word"

    # Words with spaces and special chars
    assert roundtrip(["hello world", "foo\nbar", "tab\there"]) == ["hello world", "foo\nbar", "tab\there"], "special chars"

    # Numeric strings
    assert roundtrip(["123", "456#789", "0"]) == ["123", "456#789", "0"], "numeric strings"

    # Long word
    assert roundtrip(["x" * 10000]) == ["x" * 10000], "long word"

    # Verify encoded format
    encoded = codec.encode(["hello", "world"])
    assert encoded == "5#hello5#world", "encoded format check"

    print("✅ All tests passed!")
