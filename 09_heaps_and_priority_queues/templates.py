"""Heaps & Priority Queues — Reusable Templates"""
import heapq
from typing import List
from collections import Counter


# --- Top K Frequent ---
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    return heapq.nlargest(k, Counter(nums).keys(), key=Counter(nums).get)


# --- Kth Largest (Min-Heap of size K) ---
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# --- Two Heaps: Find Median from Data Stream ---
class MedianFinder:
    def __init__(self):
        self.lo = []  # Max-heap (negate values)
        self.hi = []  # Min-heap
    
    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
    
    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2.0


# --- K Closest Points to Origin ---
def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """Max-heap of size K (negate distances)."""
    heap = []
    for x, y in points:
        dist = -(x*x + y*y)
        if len(heap) < k:
            heapq.heappush(heap, (dist, x, y))
        else:
            heapq.heappushpop(heap, (dist, x, y))
    return [[x, y] for _, x, y in heap]


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1); mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0
    
    kl = KthLargest(3, [4, 5, 8, 2])
    assert kl.add(3) == 4
    assert kl.add(5) == 5
    
    print("✅ All heap templates passed!")
