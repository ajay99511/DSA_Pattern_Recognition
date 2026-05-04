# Two Pointers

## 🎯 When to Use This Pattern

**Signal words**: "sorted array", "pair with sum", "remove duplicates", "container with water", "three sum", "move zeroes", "palindrome"

**Input characteristics**:
- Array is **sorted** (or can be sorted without losing info)
- Need to find pairs/triplets satisfying a condition
- Need to partition or rearrange elements in-place
- Comparing elements from opposite ends

## 🧠 Core Concept

Use two pointers moving through the array to avoid nested loops. Three sub-patterns:

1. **Opposite-Direction** — Start from both ends, move inward (sorted pair finding)
2. **Same-Direction (Fast/Slow)** — Both start at beginning, fast moves ahead (remove duplicates, partition)
3. **Three Pointers** — Fix one, use two-pointer on the rest (3Sum)

## 📐 Templates

### Template 1: Opposite-Direction (Pair Finding in Sorted Array)
```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### Template 2: Same-Direction (Remove Duplicates / Partition)
```python
def remove_duplicates(nums):
    if not nums: return 0
    slow = 0  # Points to last unique element
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

### Template 3: Three Sum (Fix one + Two Pointer)
```python
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: continue  # Skip duplicates
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
```

## ⚡ Variations

| Variation | Pointer Movement | Example |
|-----------|-----------------|---------|
| Opposite ends, sorted | Both inward | Two Sum II, Container With Water |
| Same direction, slow/fast | Fast always advances | Remove Duplicates, Move Zeroes |
| Fix one + two pointer | Outer loop + inner pair | 3Sum, 3Sum Closest |
| Palindrome check | Both inward, compare | Valid Palindrome |

## 🏋️ Practice Problems

| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #125 Valid Palindrome | Easy | Opposite pointers, skip non-alphanumeric |
| 2 | LC #167 Two Sum II | Easy | Sorted → opposite direction pointers |
| 3 | LC #15 3Sum | Medium | Sort + fix one + two pointer on rest |
| 4 | LC #11 Container With Water | Medium | Opposite pointers, move the shorter side |
| 5 | LC #283 Move Zeroes | Easy | Same-direction: slow=placement, fast=scanner |
| 6 | LC #26 Remove Duplicates | Easy | Same-direction in sorted array |
| 7 | LC #75 Sort Colors | Medium | Dutch National Flag: 3 pointers |
| 8 | LC #42 Trapping Rain Water | Hard | Opposite pointers tracking max heights |

## 🔗 Related Patterns
- **Sliding Window**: Same-direction pointers with a "window" between them
- **Binary Search**: Also works on sorted arrays, but for different query types
- **Fast & Slow Pointers** (Linked Lists): Same concept applied to linked lists
