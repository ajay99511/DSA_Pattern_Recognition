"""
## Problem: Trapping Rain Water (LC #42)
- **Pattern**: Two Pointers - Opposite Direction
- **Difficulty**: Hard
- **Key Insight**: Water at any position is bounded by min(max_left, max_right); process the side with the smaller max first — that side's water level is already determined regardless of what's on the other side.
- **Recognition Signal**: "trap water between bars" / "elevation map" → opposite-direction pointers; process the side with the smaller running max to avoid needing precomputed arrays
- **Complexity**: Time O(N), Space O(1)
- **My Confidence**: 🔴
- **Review Dates**: [date1] → [date2] → [date3]
"""

# Problem: Given n non-negative integers representing an elevation map where the
# width of each bar is 1, compute how much water it can trap after raining.

# STEP-BY-STEP APPROACH:
# 1. left = 0, right = n-1, left_max = 0, right_max = 0, water = 0.
# 2. While left < right:
#    a. If height[left] < height[right]:
#       - If height[left] >= left_max → update left_max (no water here, it's a new max).
#       - Else → water += left_max - height[left] (water is trapped up to left_max).
#       - left++.
#    b. Else (height[right] <= height[left]):
#       - If height[right] >= right_max → update right_max.
#       - Else → water += right_max - height[right].
#       - right--.
# 3. Return water.

# NOTE: The key insight — when height[left] < height[right], we know the
# right side has at least height[right] as a wall. So the water at left is
# determined solely by left_max (the smaller side). We don't need to know
# the actual right maximum because height[right] is already tall enough.

from typing import List


def trap(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    left_max = right_max = 0               # WHY: track running max from each side
    water = 0

    while left < right:
        if height[left] < height[right]:
            # WHY process left: right side is taller, so left_max determines water level here
            if height[left] >= left_max:
                left_max = height[left]    # WHY: new left max; no water trapped at this bar
            else:
                water += left_max - height[left]  # WHY: water fills up to left_max
            left += 1

        else:
            # WHY process right: left side is taller (or equal), so right_max determines water level
            if height[right] >= right_max:
                right_max = height[right]  # WHY: new right max; no water trapped at this bar
            else:
                water += right_max - height[right]  # WHY: water fills up to right_max
            right -= 1

    return water


# TEST CASES:
if __name__ == "__main__":
    # Classic LC example
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "classic: 6 units"

    # Another LC example
    assert trap([4, 2, 0, 3, 2, 5]) == 9,                    "second example: 9 units"

    # No water — monotonically increasing
    assert trap([1, 2, 3, 4, 5]) == 0,                       "increasing: no water"

    # No water — monotonically decreasing
    assert trap([5, 4, 3, 2, 1]) == 0,                       "decreasing: no water"

    # Single valley
    assert trap([3, 0, 3]) == 3,                             "single valley: 3 units"

    # Flat bottom
    assert trap([2, 0, 0, 0, 2]) == 6,                       "flat bottom: 6 units"

    print("✅ All tests passed!")
