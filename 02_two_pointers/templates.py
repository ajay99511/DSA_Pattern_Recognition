"""Two Pointers — Reusable Templates"""
from typing import List


# ============================================================
# TEMPLATE 1: Opposite Direction (Sorted Array)
# ============================================================
# USE WHEN: Sorted array, find pair satisfying condition
# TIME: O(N)  SPACE: O(1)

def two_sum_sorted(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target: return [left, right]
        elif s < target: left += 1
        else: right -= 1
    return []


def container_with_most_water(height: List[int]) -> int:
    """Move the SHORTER pointer inward — keeping the taller one
    can only help, never hurt."""
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


def trapping_rain_water(height: List[int]) -> int:
    """Two pointer approach — track left_max and right_max."""
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water


# ============================================================
# TEMPLATE 2: Same Direction (Slow/Fast)
# ============================================================
# USE WHEN: In-place removal, partitioning, deduplication
# TIME: O(N)  SPACE: O(1)

def remove_duplicates_sorted(nums: List[int]) -> int:
    if not nums: return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


def move_zeroes(nums: List[int]) -> None:
    """Move all zeroes to end, maintain relative order of non-zeroes."""
    slow = 0  # Next position for non-zero
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


# ============================================================
# TEMPLATE 3: Fix One + Two Pointer (3Sum Family)
# ============================================================
# USE WHEN: Triplet/quadruplet finding
# TIME: O(N²)  SPACE: O(1) extra

def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]: left += 1
                while left < right and nums[right] == nums[right-1]: right -= 1
                left += 1; right -= 1
            elif total < 0: left += 1
            else: right -= 1
    return result


# ============================================================
# TEMPLATE 4: Palindrome Check
# ============================================================

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum(): left += 1
        while left < right and not s[right].isalnum(): right -= 1
        if s[left].lower() != s[right].lower(): return False
        left += 1; right -= 1
    return True


if __name__ == "__main__":
    assert two_sum_sorted([2,7,11,15], 9) == [0, 1]
    assert container_with_most_water([1,8,6,2,5,4,8,3,7]) == 49
    assert trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    
    nums = [0,1,0,3,12]
    move_zeroes(nums)
    assert nums == [1,3,12,0,0]
    
    print("✅ All two pointers templates passed!")
