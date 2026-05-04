"""Linked Lists — Reusable Templates"""
from typing import Optional, List
from heapq import heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# --- Fast & Slow Pointers ---
def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast: return True
    return False

def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow


# --- Reverse ---
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    return prev


# --- Merge Two Sorted ---
def merge_two_lists(l1, l2):
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next


# --- Merge K Sorted (Heap) ---
def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = curr = ListNode(0)
    heap = []
    for i, node in enumerate(lists):
        if node:
            heappush(heap, (node.val, i, node))
    while heap:
        val, i, node = heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heappush(heap, (node.next.val, i, node.next))
    return dummy.next


# --- Remove Nth From End ---
def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n + 1): fast = fast.next
    while fast:
        slow, fast = slow.next, fast.next
    slow.next = slow.next.next
    return dummy.next


# --- Reorder List: L0→Ln→L1→Ln-1→... ---
def reorder_list(head: Optional[ListNode]) -> None:
    if not head or not head.next: return
    # 1. Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
    # 2. Reverse second half
    second = reverse_list(slow.next)
    slow.next = None
    # 3. Merge alternating
    first = head
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next, second.next = second, tmp1
        first, second = tmp1, tmp2


def _to_list(head):
    """Helper: linked list → python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def _from_list(arr):
    """Helper: python list → linked list."""
    dummy = curr = ListNode(0)
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    # Reverse
    head = _from_list([1,2,3,4,5])
    assert _to_list(reverse_list(head)) == [5,4,3,2,1]
    
    # Merge
    l1 = _from_list([1,3,5])
    l2 = _from_list([2,4,6])
    assert _to_list(merge_two_lists(l1, l2)) == [1,2,3,4,5,6]
    
    # Cycle detection
    assert has_cycle(_from_list([1,2,3])) == False
    
    print("✅ All linked list templates passed!")
