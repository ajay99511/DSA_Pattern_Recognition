"""Intervals — Reusable Templates"""
from typing import List
import heapq


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def insert_interval(intervals: List[List[int]], new: List[int]) -> List[List[int]]:
    result = []
    for i, (s, e) in enumerate(intervals):
        if e < new[0]:
            result.append([s, e])
        elif s > new[1]:
            result.append(new)
            return result + intervals[i:]
        else:
            new = [min(s, new[0]), max(e, new[1])]
    result.append(new)
    return result


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    intervals.sort()
    heap = []
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """LC #435 — Sort by end time, greedily keep non-overlapping."""
    intervals.sort(key=lambda x: x[1])
    count = 0
    prev_end = float('-inf')
    for s, e in intervals:
        if s >= prev_end:
            prev_end = e
        else:
            count += 1
    return count


if __name__ == "__main__":
    assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert insert_interval([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert min_meeting_rooms([[0,30],[5,10],[15,20]]) == 2
    assert erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    print("✅ All interval templates passed!")
