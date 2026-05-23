"""
Two Pointers — Reusable Templates
===================================
Three production-quality O(N) templates for FAANG interview preparation.

  1. OPPOSITE DIRECTION  — converging pointers for sorted arrays, pair sum,
                           container problems, palindrome checks
  2. SAME DIRECTION      — fast/slow write pointer for remove duplicates,
                           partition in-place, cycle detection
  3. PARTITION           — Dutch National Flag / 3-way partition for
                           sort colors, 3-way quicksort pivot, k-groups

Each template includes:
  • Recognition signals  — problem keywords that trigger this template
  • Annotated skeleton   — every line explained with WHY, not just WHAT
  • Concrete example     — a worked LeetCode problem with trace
  • Complexity           — Time O(N) and Space O(1) annotations
  • Runnable assertions  — verified in __main__

Run with:  python templates.py
"""

from typing import List, Optional


# ============================================================
# TEMPLATE 1: OPPOSITE DIRECTION (Converging Pointers)
# ============================================================
#
# RECOGNITION SIGNALS
# -------------------
#   "sorted array" + "find pair / triplet"
#   "two sum" / "three sum" on a sorted input
#   "container with most water" / "maximize area"
#   "trapping rain water"
#   "palindrome" / "valid palindrome"
#   "reverse" / "two endpoints"
#   Any problem where moving one pointer inward is provably safe
#
# CORE IDEA
# ---------
#   left = 0, right = n-1.  Both pointers move INWARD toward each other.
#   Sorted order gives a monotonic relationship:
#     • moving left  right  always increases the pair sum
#     • moving right left   always decreases the pair sum
#   Each step eliminates one candidate with certainty → O(N) total.
#   No element is visited more than once.
#
# SKELETON
# --------
#   left, right = 0, len(arr) - 1
#   while left < right:
#       value = f(arr[left], arr[right])   # compute something from both ends
#       if value == target:
#           # found answer
#       elif value < target:
#           left  += 1   # need a larger value → move left pointer right
#       else:
#           right -= 1   # need a smaller value → move right pointer left
#
# COMPLEXITY: Time O(N)  |  Space O(1)
# ============================================================


def two_sum_sorted(nums: List[int], target: int) -> List[int]:
    """
    LC #167 — Two Sum II (sorted input array).
    Return 1-indexed [left+1, right+1] of the pair that sums to target.

    WHY opposite direction: the array is sorted, so we have a monotonic
    relationship between pointer positions and pair sums.  Moving left
    right increases the sum; moving right left decreases it.  We can
    eliminate one candidate per step → O(N) instead of O(N²).

    Trace: nums = [2, 7, 11, 15], target = 9
      left=0(2), right=3(15) → sum=17 > 9 → right--
      left=0(2), right=2(11) → sum=13 > 9 → right--
      left=0(2), right=1(7)  → sum=9 == 9 → return [1, 2]  ✓

    Complexity: Time O(N) — each pointer moves at most N steps total.
                Space O(1) — only two index variables.
    """
    left, right = 0, len(nums) - 1          # WHY both ends: sorted array, converge inward

    while left < right:                      # WHY strict <: pointers must not cross (same element)
        curr_sum = nums[left] + nums[right]

        if curr_sum == target:
            return [left + 1, right + 1]     # WHY +1: LC #167 uses 1-indexed output

        elif curr_sum < target:
            left += 1                        # WHY left++: sum too small; only a larger left value helps
                                             # (right is already the largest available partner)
        else:
            right -= 1                       # WHY right--: sum too large; only a smaller right value helps
                                             # (left is already the smallest available partner)

    return []                                # WHY []: problem guarantees a solution exists; unreachable


def container_with_most_water(height: List[int]) -> int:
    """
    LC #11 — Container With Most Water.
    Area = min(height[L], height[R]) * (R - L).
    Always move the SHORTER wall inward.

    WHY move the shorter wall: moving the taller wall inward can only
    decrease width (bad) while the height is still capped by the shorter
    wall (no gain) → strictly worse.  Moving the shorter wall inward
    decreases width but might find a taller wall → only hope for gain.

    Trace: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
      left=0(1), right=8(7) → area=1*8=8  → move left (shorter)
      left=1(8), right=8(7) → area=7*7=49 → move right (shorter)
      ... best = 49

    Complexity: Time O(N).  Space O(1).
    """
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left                          # WHY: distance between walls
        area  = min(height[left], height[right]) * width
        max_area = max(max_area, area)                # WHY: track running maximum

        if height[left] < height[right]:
            left  += 1                                # WHY: left wall is the bottleneck; move it
        else:
            right -= 1                                # WHY: right wall is bottleneck (or equal); move it

    return max_area


def is_palindrome(s: str) -> bool:
    """
    LC #125 — Valid Palindrome (alphanumeric only, case-insensitive).
    Compare characters from both ends, skipping non-alphanumeric.

    WHY opposite direction: a palindrome reads the same forwards and
    backwards.  Comparing from both ends simultaneously is the most
    direct check and terminates as soon as a mismatch is found.

    Trace: "A man, a plan, a canal: Panama"
      left='A', right='a' → match (case-insensitive) → move both inward
      skip spaces/commas ... → all characters match → True

    Complexity: Time O(N).  Space O(1).
    """
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():   # WHY: skip non-alphanumeric from left
            left += 1
        while left < right and not s[right].isalnum():  # WHY: skip non-alphanumeric from right
            right -= 1

        if s[left].lower() != s[right].lower():         # WHY lower(): case-insensitive comparison
            return False                                 # WHY: mismatch → not a palindrome

        left  += 1                                       # WHY: matched pair; advance both inward
        right -= 1

    return True                                          # WHY: all pairs matched → palindrome


# ============================================================
# TEMPLATE 2: SAME DIRECTION (Fast / Slow Write Pointer)
# ============================================================
#
# RECOGNITION SIGNALS
# -------------------
#   "remove duplicates in-place"
#   "remove element in-place" / "filter array without extra space"
#   "move zeroes to end" / "move all X to one side"
#   "partition array" / "separate even/odd"
#   "squares of sorted array" (fill from back)
#   "linked list cycle" / "find middle of linked list"
#   Any problem requiring in-place modification with O(1) extra space
#
# CORE IDEA
# ---------
#   slow = write pointer  (next slot in the "clean" output prefix)
#   fast = read  pointer  (scans every element exactly once)
#
#   Invariant: nums[0 .. slow-1] is always the valid output prefix.
#   fast always advances by 1 each iteration.
#   slow only advances when a condition is met (element is "kept").
#
# SKELETON
# --------
#   slow = 0
#   for fast in range(len(nums)):
#       if should_keep(nums[fast]):        # condition varies by problem
#           nums[slow] = nums[fast]        # write the kept element
#           slow += 1                      # advance write pointer
#   return slow                            # length of valid prefix
#
# COMPLEXITY: Time O(N)  |  Space O(1)
# ============================================================


def remove_duplicates_sorted(nums: List[int]) -> int:
    """
    LC #26 — Remove Duplicates from Sorted Array.
    Modify nums in-place; return the length of the deduplicated prefix.

    WHY same direction: we need to scan every element (fast) while
    maintaining a "clean" prefix of unique values (slow).  The sorted
    order guarantees that duplicates are adjacent, so comparing
    nums[fast] with nums[slow] is sufficient.

    Trace: nums = [1, 1, 2, 3, 3, 4]
      slow=0, fast=1: nums[1]=1 == nums[0]=1 → skip
      slow=0, fast=2: nums[2]=2 != nums[0]=1 → slow=1, nums[1]=2
      slow=1, fast=3: nums[3]=3 != nums[1]=2 → slow=2, nums[2]=3
      slow=2, fast=4: nums[4]=3 == nums[2]=3 → skip
      slow=2, fast=5: nums[5]=4 != nums[2]=3 → slow=3, nums[3]=4
      return 4  →  nums[:4] = [1, 2, 3, 4]  ✓

    Complexity: Time O(N).  Space O(1).
    """
    if not nums:
        return 0

    slow = 0                              # WHY slow=0: first element is always kept

    for fast in range(1, len(nums)):      # WHY start at 1: compare against the element at slow
        if nums[fast] != nums[slow]:      # WHY !=: found a new unique element
            slow += 1                     # WHY slow++: advance write pointer to next slot
            nums[slow] = nums[fast]       # WHY write: place the new unique element in the clean prefix

    return slow + 1                       # WHY +1: slow is the last valid index; length = index + 1


def remove_element(nums: List[int], val: int) -> int:
    """
    LC #27 — Remove Element.
    Remove all occurrences of val in-place; return the new length.

    WHY same direction: slow marks the next write position; fast scans
    every element.  Elements equal to val are simply skipped (fast
    advances but slow does not).

    Trace: nums = [3, 2, 2, 3], val = 3
      fast=0: nums[0]=3 == val → skip
      fast=1: nums[1]=2 != val → nums[0]=2, slow=1
      fast=2: nums[2]=2 != val → nums[1]=2, slow=2
      fast=3: nums[3]=3 == val → skip
      return 2  →  nums[:2] = [2, 2]  ✓

    Complexity: Time O(N).  Space O(1).
    """
    slow = 0                              # WHY: next write position in the clean prefix

    for fast in range(len(nums)):
        if nums[fast] != val:             # WHY: keep elements that are NOT val
            nums[slow] = nums[fast]       # WHY: write the kept element into the clean prefix
            slow += 1                     # WHY: advance write pointer

    return slow                           # WHY: slow equals the count of kept elements


def move_zeroes(nums: List[int]) -> None:
    """
    LC #283 — Move Zeroes.
    Move all 0s to the end while preserving relative order of non-zeros.
    Modifies nums in-place; returns None.

    WHY swap instead of assign: swapping automatically pushes zeros to
    the back without a second pass to fill zeros.

    Trace: nums = [0, 1, 0, 3, 12]
      fast=0: 0 → skip
      fast=1: 1 → swap(nums[0], nums[1]) → [1, 0, 0, 3, 12], slow=1
      fast=2: 0 → skip
      fast=3: 3 → swap(nums[1], nums[3]) → [1, 3, 0, 0, 12], slow=2
      fast=4: 12→ swap(nums[2], nums[4]) → [1, 3, 12, 0, 0], slow=3  ✓

    Complexity: Time O(N).  Space O(1).
    """
    slow = 0                              # WHY: next position for a non-zero element

    for fast in range(len(nums)):
        if nums[fast] != 0:               # WHY: only act on non-zero elements
            nums[slow], nums[fast] = nums[fast], nums[slow]  # WHY swap: zeros drift right automatically
            slow += 1                     # WHY: advance write pointer past the placed non-zero


# ============================================================
# TEMPLATE 3: PARTITION (Dutch National Flag / 3-Way Partition)
# ============================================================
#
# RECOGNITION SIGNALS
# -------------------
#   "sort colors" / "sort 0s, 1s, 2s"
#   "Dutch National Flag"
#   "partition array into k groups"
#   "move all negatives to left" / "separate by condition"
#   "3-way quicksort" / "equal elements in the middle"
#   "segregate" / "rearrange by value"
#   Any problem with exactly 3 categories (less / equal / greater)
#
# CORE IDEA
# ---------
#   Three pointers divide the array into four regions:
#
#     [0 .. low-1]   → region 0  (all elements < pivot, fully processed)
#     [low .. mid-1] → region 1  (all elements == pivot, fully processed)
#     [mid .. high]  → region ?  (unprocessed / unknown)
#     [high+1 .. n-1]→ region 2  (all elements > pivot, fully processed)
#
#   mid is the "cursor" that scans forward.  The loop ends when mid > high
#   (the unknown region is empty).
#
# INVARIANT (maintained at the start of every iteration)
# -------------------------------------------------------
#   nums[0 .. low-1]  == 0  (or "small")
#   nums[low .. mid-1] == 1  (or "equal")
#   nums[high+1 .. n-1] == 2 (or "large")
#   nums[mid .. high]  = unknown
#
# SKELETON
# --------
#   low, mid, high = 0, 0, len(nums) - 1
#   while mid <= high:
#       if nums[mid] == 0:                 # belongs in left region
#           swap(nums[low], nums[mid])
#           low += 1; mid += 1            # both advance: swapped-in element is known (==1)
#       elif nums[mid] == 1:               # already in correct region
#           mid += 1
#       else:                              # nums[mid] == 2: belongs in right region
#           swap(nums[mid], nums[high])
#           high -= 1                     # mid does NOT advance: swapped-in element is unknown
#
# WHY mid doesn't advance after swapping with high:
#   The element swapped in from nums[high] has not been examined yet.
#   We must inspect it before moving mid forward.
#   The element swapped out to nums[high] is known to be 2 → correct.
#
# COMPLEXITY: Time O(N) — mid advances or high shrinks each step.
#             Space O(1) — three index variables only.
# ============================================================


def sort_colors(nums: List[int]) -> None:
    """
    LC #75 — Sort Colors (Dutch National Flag).
    Sort an array of 0s, 1s, and 2s in-place in a single pass.
    Modifies nums in-place; returns None.

    WHY 3-pointer partition: a standard sort is O(N log N).  Because
    there are only 3 distinct values, we can use the DNF algorithm to
    sort in O(N) with O(1) space in a single pass.

    Trace: nums = [2, 0, 2, 1, 1, 0]
      low=0, mid=0, high=5
      mid=0: nums[0]=2 → swap(0,5) → [0,0,2,1,1,2], high=4
      mid=0: nums[0]=0 → swap(0,0) → [0,0,2,1,1,2], low=1, mid=1
      mid=1: nums[1]=0 → swap(1,1) → [0,0,2,1,1,2], low=2, mid=2
      mid=2: nums[2]=2 → swap(2,4) → [0,0,1,1,2,2], high=3
      mid=2: nums[2]=1 → mid=3
      mid=3: nums[3]=1 → mid=4
      mid=4 > high=3 → done  →  [0, 0, 1, 1, 2, 2]  ✓

    Complexity: Time O(N) — each element is processed at most once.
                Space O(1) — three pointer variables.
    """
    low  = 0                              # WHY: boundary of the 0-region (exclusive right end)
    mid  = 0                              # WHY: current element under examination
    high = len(nums) - 1                  # WHY: boundary of the 2-region (exclusive left end)

    while mid <= high:                    # WHY <=: stop when unknown region [mid..high] is empty
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]   # WHY: move 0 to left region
            low  += 1                     # WHY: expand 0-region rightward
            mid  += 1                     # WHY: element now at mid is known to be 1 (was in [low..mid-1])
        elif nums[mid] == 1:
            mid  += 1                     # WHY: 1 is already in the correct middle region; just advance
        else:                             # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid] # WHY: move 2 to right region
            high -= 1                     # WHY: expand 2-region leftward
                                          # WHY NOT mid++: swapped-in element from high is unexamined


def partition_by_pivot(nums: List[int], pivot: int) -> List[int]:
    """
    Generic 3-way partition: rearrange nums so that elements less than
    pivot come first, elements equal to pivot come second, and elements
    greater than pivot come last.  Returns the modified array.

    This is the core of 3-way quicksort (Dijkstra's DNF algorithm).

    WHY 3-way instead of 2-way: when many elements equal the pivot,
    2-way partition degrades to O(N²) on repeated elements.  3-way
    partition handles duplicates in O(N) by placing all equal elements
    in the middle in a single pass.

    Trace: nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3], pivot = 3
      After partition: [1, 1, 2, 3, 3, 5, 9, 4, 6, 5]  (order within groups may vary)
      All elements < 3 are left of all elements == 3, which are left of all > 3.

    Complexity: Time O(N).  Space O(1) in-place.
    """
    low  = 0
    mid  = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] < pivot:
            nums[low], nums[mid] = nums[mid], nums[low]
            low  += 1
            mid  += 1
        elif nums[mid] == pivot:
            mid  += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums                           # WHY return: convenience for testing; mutation is in-place


def segregate_negatives(nums: List[int]) -> List[int]:
    """
    Move all negative numbers to the left, non-negatives to the right.
    Relative order within each group is NOT guaranteed (in-place swap).

    WHY 2-pointer partition suffices here: only 2 groups (negative /
    non-negative), so we don't need the full 3-pointer DNF.  This is
    the classic Lomuto/Hoare-style partition reduced to 2 categories.

    Trace: nums = [-3, 1, -2, 4, -1, 5]
      slow=0, fast=0: -3 < 0 → swap(0,0), slow=1
      slow=1, fast=1:  1 ≥ 0 → skip
      slow=1, fast=2: -2 < 0 → swap(1,2) → [-3,-2,1,4,-1,5], slow=2
      slow=2, fast=3:  4 ≥ 0 → skip
      slow=2, fast=4: -1 < 0 → swap(2,4) → [-3,-2,-1,4,1,5], slow=3
      slow=3, fast=5:  5 ≥ 0 → skip
      Result: [-3, -2, -1, 4, 1, 5]  ✓ (all negatives left)

    Complexity: Time O(N).  Space O(1).
    """
    slow = 0                              # WHY: boundary of the negative region

    for fast in range(len(nums)):
        if nums[fast] < 0:                # WHY: negative elements belong in the left region
            nums[slow], nums[fast] = nums[fast], nums[slow]  # WHY swap: move negative to boundary
            slow += 1                     # WHY: expand negative region

    return nums                           # WHY return: convenience for testing


# ============================================================
# MAIN — Runnable assertions for all three templates
# ============================================================

if __name__ == "__main__":

    # ── Template 1: Opposite Direction ───────────────────────

    # two_sum_sorted: basic case
    assert two_sum_sorted([2, 7, 11, 15], 9)  == [1, 2], "two_sum_sorted basic"
    # two_sum_sorted: complement appears in the middle
    assert two_sum_sorted([2, 3, 4], 6)        == [1, 3], "two_sum_sorted middle"
    # two_sum_sorted: adjacent pair
    assert two_sum_sorted([-1, 0], -1)         == [1, 2], "two_sum_sorted negative"
    # two_sum_sorted: same value used (different indices)
    assert two_sum_sorted([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5], "two_sum_sorted dup values"

    # container_with_most_water
    assert container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, "container basic"
    assert container_with_most_water([1, 1])                        == 1,  "container two walls"
    assert container_with_most_water([4, 3, 2, 1, 4])              == 16, "container equal ends"

    # is_palindrome
    assert is_palindrome("A man, a plan, a canal: Panama") is True,  "palindrome classic"
    assert is_palindrome("race a car")                      is False, "palindrome false"
    assert is_palindrome("")                                is True,  "palindrome empty"
    assert is_palindrome(".,")                              is True,  "palindrome only punctuation"
    assert is_palindrome("0P")                              is False, "palindrome mixed alnum"

    print("✅ Template 1 (Opposite Direction) — all assertions passed")

    # ── Template 2: Same Direction ────────────────────────────

    # remove_duplicates_sorted
    nums = [1, 1, 2]
    k = remove_duplicates_sorted(nums)
    assert k == 2 and nums[:k] == [1, 2], "remove_dup [1,1,2]"

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates_sorted(nums)
    assert k == 5 and nums[:k] == [0, 1, 2, 3, 4], "remove_dup long"

    nums = [1]
    k = remove_duplicates_sorted(nums)
    assert k == 1 and nums[:k] == [1], "remove_dup single element"

    # remove_element
    nums = [3, 2, 2, 3]
    k = remove_element(nums, 3)
    assert k == 2 and sorted(nums[:k]) == [2, 2], "remove_element basic"

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = remove_element(nums, 2)
    assert k == 5 and sorted(nums[:k]) == [0, 0, 1, 3, 4], "remove_element multiple"

    nums = [1]
    k = remove_element(nums, 1)
    assert k == 0, "remove_element all removed"

    # move_zeroes
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    assert nums == [1, 3, 12, 0, 0], "move_zeroes basic"

    nums = [0]
    move_zeroes(nums)
    assert nums == [0], "move_zeroes single zero"

    nums = [1, 2, 3]
    move_zeroes(nums)
    assert nums == [1, 2, 3], "move_zeroes no zeros"

    nums = [0, 0, 0, 1]
    move_zeroes(nums)
    assert nums == [1, 0, 0, 0], "move_zeroes leading zeros"

    print("✅ Template 2 (Same Direction) — all assertions passed")

    # ── Template 3: Partition ─────────────────────────────────

    # sort_colors: standard LC #75 examples
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2], "sort_colors basic"

    nums = [2, 0, 1]
    sort_colors(nums)
    assert nums == [0, 1, 2], "sort_colors three elements"

    nums = [0]
    sort_colors(nums)
    assert nums == [0], "sort_colors single 0"

    nums = [1, 1, 1]
    sort_colors(nums)
    assert nums == [1, 1, 1], "sort_colors all same"

    nums = [2, 2, 0, 0, 1, 1]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2], "sort_colors interleaved"

    # partition_by_pivot: verify ordering invariant
    nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    result = partition_by_pivot(nums, 3)
    # Find the boundary indices
    first_non_small = next((i for i, x in enumerate(result) if x >= 3), len(result))
    first_large     = next((i for i, x in enumerate(result) if x > 3),  len(result))
    assert all(x < 3 for x in result[:first_non_small]),          "partition: left region < pivot"
    assert all(x == 3 for x in result[first_non_small:first_large]), "partition: mid region == pivot"
    assert all(x > 3 for x in result[first_large:]),              "partition: right region > pivot"

    # partition_by_pivot: all equal
    nums = [5, 5, 5]
    result = partition_by_pivot(nums, 5)
    assert result == [5, 5, 5], "partition all equal"

    # partition_by_pivot: pivot not present
    nums = [1, 3, 5, 7]
    result = partition_by_pivot(nums, 4)
    assert all(x < 4 for x in result[:2]) and all(x > 4 for x in result[2:]), \
        "partition pivot absent"

    # segregate_negatives: all negatives on the left
    nums = [-3, 1, -2, 4, -1, 5]
    result = segregate_negatives(nums)
    neg_count = sum(1 for x in result if x < 0)
    assert all(x < 0 for x in result[:neg_count]),  "segregate: left region all negative"
    assert all(x >= 0 for x in result[neg_count:]), "segregate: right region all non-negative"
    assert sorted(result) == sorted([-3, 1, -2, 4, -1, 5]), "segregate: no elements lost"

    nums = [1, 2, 3]
    result = segregate_negatives(nums)
    assert all(x >= 0 for x in result), "segregate: no negatives"

    nums = [-1, -2, -3]
    result = segregate_negatives(nums)
    assert all(x < 0 for x in result), "segregate: all negatives"

    print("✅ Template 3 (Partition) — all assertions passed")

    print()
    print("🎉 All two-pointer templates passed!")
