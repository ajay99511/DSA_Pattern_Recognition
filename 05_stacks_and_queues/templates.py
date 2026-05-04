"""Stacks & Queues — Reusable Templates"""
from typing import List
from collections import deque


def is_valid_parentheses(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in pairs:
            if not stack or stack[-1] != pairs[c]: return False
            stack.pop()
        else:
            stack.append(c)
    return not stack


class MinStack:
    """LC #155 — Stack that supports O(1) getMin."""
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))
    
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    
    def top(self): return self.stack[-1]
    def getMin(self): return self.min_stack[-1]


def daily_temperatures(temps: List[int]) -> List[int]:
    """LC #739 — Monotonic decreasing stack."""
    result = [0] * len(temps)
    stack = []  # Indices
    for i in range(len(temps)):
        while stack and temps[stack[-1]] < temps[i]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result


def largest_rectangle_histogram(heights: List[int]) -> int:
    """LC #84 — Monotonic increasing stack. O(N)."""
    stack = [-1]  # Sentinel
    max_area = 0
    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    while stack[-1] != -1:
        h = heights[stack.pop()]
        w = len(heights) - stack[-1] - 1
        max_area = max(max_area, h * w)
    return max_area


def eval_rpn(tokens: List[str]) -> int:
    """LC #150 — Evaluate Reverse Polish Notation."""
    stack = []
    for t in tokens:
        if t in {'+', '-', '*', '/'}:
            b, a = stack.pop(), stack.pop()
            if t == '+': stack.append(a + b)
            elif t == '-': stack.append(a - b)
            elif t == '*': stack.append(a * b)
            else: stack.append(int(a / b))  # Truncate toward zero
        else:
            stack.append(int(t))
    return stack[0]


if __name__ == "__main__":
    assert is_valid_parentheses("()[]{}") == True
    assert is_valid_parentheses("(]") == False
    assert daily_temperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert largest_rectangle_histogram([2,1,5,6,2,3]) == 10
    assert eval_rpn(["2","1","+","3","*"]) == 9
    print("✅ All stacks & queues templates passed!")
