"""
## Problem: Product of Array Except Self (LC #238)
- **Pattern**: Arrays & Hashing - Prefix/Suffix Product
- **Difficulty**: Medium
- **Key Insight**: result[i] = (product of all elements LEFT of i) × (product of all elements RIGHT of i); compute left products in a forward pass and right products in a backward pass, reusing the output array to achieve O(1) extra space.
- **Recognition Signal**: "product except self" / "no division allowed" / "prefix product" → two-pass prefix/suffix
- **Complexity**: Time O(N), Space O(1) extra (output array doesn't count per problem statement)
- **My Confidence**: 🟢
- **Review Dates**: [date1] → [date2] → [date3]
"""

# STEP-BY-STEP APPROACH:
# 1. Initialize result array of size N with all 1s.
# 2. Forward pass (left products):
#    - Maintain a running prefix product (starts at 1).
#    - result[i] = prefix (product of everything to the left of i).
#    - Update prefix *= nums[i] after storing.
# 3. Backward pass (right products):
#    - Maintain a running suffix product (starts at 1).
#    - result[i] *= suffix (multiply in the product of everything to the right of i).
#    - Update suffix *= nums[i] after multiplying.
# 4. Return result.

# WHY no division: handles zeros correctly and satisfies the problem constraint.

# SOLUTION:
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n                    # Will hold left products, then final answer

        # --- Forward pass: result[i] = product of nums[0..i-1] ---
        prefix = 1
        for i in range(n):
            result[i] = prefix              # Store left product before including nums[i]
            prefix *= nums[i]               # Extend prefix to include nums[i]

        # --- Backward pass: multiply result[i] by product of nums[i+1..n-1] ---
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix             # Combine left product with right product
            suffix *= nums[i]               # Extend suffix to include nums[i]

        return result


# TEST CASES:
if __name__ == "__main__":
    s = Solution()

    # Classic example
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6], "classic [1,2,3,4]"

    # Contains a zero — all products involving the zero position become 0
    # except the position of the zero itself (which gets the product of all others)
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0], "contains zero"

    # Two zeros — every product is 0
    assert s.productExceptSelf([0, 0]) == [0, 0], "two zeros"

    # Two elements
    assert s.productExceptSelf([3, 4]) == [4, 3], "two elements"

    # Single element — product of empty set = 1
    assert s.productExceptSelf([5]) == [1], "single element"

    # All ones
    assert s.productExceptSelf([1, 1, 1, 1]) == [1, 1, 1, 1], "all ones"

    # Negative numbers: [-2*-3, -1*-3, -1*-2] = [6, 3, 2]
    assert s.productExceptSelf([-1, -2, -3]) == [6, 3, 2], "negatives"

    print("✅ All tests passed!")
