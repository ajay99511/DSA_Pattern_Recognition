# Stacks & Queues

## 🎯 When to Use This Pattern
**Signal words**: "valid parentheses", "next greater/smaller element", "daily temperatures", "evaluate expression", "monotonic", "decode string"

## 📐 Templates

### Template 1: Matching/Validation (Parentheses)
```python
def is_valid(s):
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}
    for c in s:
        if c in pairs:
            if not stack or stack[-1] != pairs[c]: return False
            stack.pop()
        else:
            stack.append(c)
    return not stack
```

### Template 2: Monotonic Stack (Next Greater Element)
```python
def next_greater_element(nums):
    result = [-1] * len(nums)
    stack = []  # Stores indices, values are decreasing
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
```

### Template 3: Monotonic Decreasing Deque (Sliding Window Max)
```python
from collections import deque
def max_sliding_window(nums, k):
    dq = deque()  # Indices with decreasing values
    result = []
    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1: dq.popleft()
        while dq and nums[dq[-1]] < nums[i]: dq.pop()
        dq.append(i)
        if i >= k - 1: result.append(nums[dq[0]])
    return result
```

## 🏋️ Practice Problems
| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #20 Valid Parentheses | Easy | Stack matching |
| 2 | LC #155 Min Stack | Medium | Two stacks: main + mins |
| 3 | LC #150 Reverse Polish Notation | Medium | Stack evaluation |
| 4 | LC #739 Daily Temperatures | Medium | Monotonic decreasing stack |
| 5 | LC #496 Next Greater Element I | Easy | Monotonic stack + hash map |
| 6 | LC #853 Car Fleet | Medium | Sort + stack for merge detection |
| 7 | LC #84 Largest Rectangle Histogram | Hard | Monotonic increasing stack |
| 8 | LC #394 Decode String | Medium | Stack for nested brackets |
| 9 | LC #42 Trapping Rain Water | Hard | Monotonic stack approach |
