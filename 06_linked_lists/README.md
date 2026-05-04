# Linked Lists

## 🎯 When to Use This Pattern
**Signal words**: "cycle", "middle", "merge sorted", "reverse", "Nth from end", "palindrome", "reorder"

## 📐 Templates

### Template 1: Fast & Slow Pointers
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # Middle node (right-middle for even length)
```

### Template 2: Reverse a Linked List
```python
def reverse_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev  # New head
```

### Template 3: Merge Two Sorted Lists
```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1; l1 = l1.next
        else:
            curr.next = l2; l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next
```

## 🏋️ Practice Problems
| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #206 Reverse Linked List | Easy | 3-pointer iterative |
| 2 | LC #21 Merge Two Sorted Lists | Easy | Dummy head technique |
| 3 | LC #141 Linked List Cycle | Easy | Fast/slow pointers |
| 4 | LC #143 Reorder List | Medium | Find mid → reverse 2nd half → merge |
| 5 | LC #19 Remove Nth From End | Medium | Two pointers with gap N |
| 6 | LC #138 Copy List with Random | Medium | Hash map: old node → new node |
| 7 | LC #23 Merge K Sorted Lists | Hard | Min-heap of list heads |
