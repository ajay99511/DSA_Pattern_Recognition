# Intervals

## 🎯 When to Use
**Signal words**: "intervals", "overlapping", "merge", "meeting rooms", "insert", "schedule"

**Rule #1**: ALWAYS sort intervals first (usually by start time).

## 📐 Templates

### Merge Intervals
```python
def merge(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

### Meeting Rooms II (Min Rooms Needed)
```python
import heapq
def min_meeting_rooms(intervals):
    intervals.sort()
    heap = []  # End times of ongoing meetings
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)
```

## 🏋️ Practice Problems
| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #252 Meeting Rooms | Easy | Sort, check no overlap |
| 2 | LC #56 Merge Intervals | Medium | Sort by start, extend end |
| 3 | LC #57 Insert Interval | Medium | Find overlap range, merge |
| 4 | LC #253 Meeting Rooms II | Medium | Min-heap of end times |
| 5 | LC #435 Non-overlapping Intervals | Medium | Sort by end, count removals |
| 6 | LC #1851 Min Interval to Include Query | Hard | Sort + sweep line + heap |
