# Heaps & Priority Queues

## 🎯 When to Use
**Signal words**: "Kth largest/smallest", "top K", "merge K sorted", "median stream", "schedule", "closest points"

## 📐 Templates

### Top K Elements
```python
import heapq
def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

### Merge K Sorted (see linked lists)
### Two Heaps for Median
```python
class MedianFinder:
    def __init__(self):
        self.lo = []  # max-heap (negate values)
        self.hi = []  # min-heap
    def addNum(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```

## 🏋️ Practice Problems
| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #703 Kth Largest Element Stream | Easy | Min-heap of size K |
| 2 | LC #347 Top K Frequent Elements | Medium | Counter + heap/bucket sort |
| 3 | LC #973 K Closest Points to Origin | Medium | Max-heap of size K |
| 4 | LC #621 Task Scheduler | Medium | Max-heap + greedy cooldown |
| 5 | LC #355 Design Twitter | Medium | Merge K feeds with heap |
| 6 | LC #295 Find Median from Stream | Hard | Two heaps (max + min) |
| 7 | LC #23 Merge K Sorted Lists | Hard | Min-heap of heads |
