"""
## Problem: Container With Most Water (LC #11)
- **Pattern**: Two Pointers - Opposite Direction
- **Difficulty**: Medium
- **Key Insight**: Always move the shorter wall inward — moving the taller wall can only decrease width while the height is still capped by the shorter wall, so it can never improve the area.
- **Recognition Signal**: "maximize area between two lines" / "container" / "water" → opposite-direction pointers; greedy move of the shorter wall
- **Complexity**: Time O(N), Space O(1)
- **My Confidence**: 🟢
- **Review Dates**: [date1] → [date2] → [date3]
"""

# Problem: Given n non-negative integers representing heights of vertical lines,
# find two lines that together with the x-axis form a container that holds the
# most water. Return the maximum amount of water the container can store.
# Area = min(height[left], height[right]) * (right - left).

# STEP-BY-STEP APPROACH:
# 1. left = 0, right = n-1, max_area = 0.
# 2. While left < right:
#    a. Compute area = min(height[left], height[right]) * (right - left).
#    b. Update max_area.
#    c. Move the pointer pointing to the shorter wall inward.
#       (If equal, move either — moving right is conventional.)
# 3. Return max_area.

# NOTE: The greedy proof — if we move the taller wall, width decreases and
# height is still bounded by the shorter wall → area cannot increase.
# Moving the shorter wall is the only way to potentially find a taller wall
# that compensates for the reduced width.

from typing import List


def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        width = right - left                              # WHY: horizontal distance between walls
        area  = min(height[left], height[right]) * width  # WHY min: water level is capped by shorter wall
        best  = max(best, area)                           # WHY: track running maximum

        if height[left] < height[right]:
            left  += 1                                    # WHY: left is the bottleneck; move it inward
        else:
            right -= 1                                    # WHY: right is bottleneck (or equal); move it

    return best


# TEST CASES:
if __name__ == "__main__":
    # Classic LC example
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, "classic: walls at index 1 and 8"

    # Two walls only
    assert max_area([1, 1]) == 1,                        "two walls"

    # Equal height walls at the ends
    assert max_area([4, 3, 2, 1, 4]) == 16,              "equal ends: 4*4=16"

    # Increasing heights — best is the last two
    assert max_area([1, 2, 3, 4, 5]) == 6,               "increasing: 2*3=6 (indices 1,4)"

    # Single tall wall in the middle
    assert max_area([1, 100, 1]) == 2,                   "tall middle: min(1,1)*2=2"

    print("✅ All tests passed!")
