"""Trees — Reusable Templates"""
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


# --- DFS: Max Depth ---
def max_depth(root: Optional[TreeNode]) -> int:
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# --- DFS: Validate BST ---
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def helper(node, lo, hi):
        if not node: return True
        if not (lo < node.val < hi): return False
        return helper(node.left, lo, node.val) and helper(node.right, node.val, hi)
    return helper(root, float('-inf'), float('inf'))


# --- DFS: Lowest Common Ancestor ---
def lca(root, p, q):
    if not root or root == p or root == q: return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right: return root
    return left or right


# --- DFS: Diameter (track global max) ---
def diameter(root: Optional[TreeNode]) -> int:
    max_d = [0]
    def depth(node):
        if not node: return 0
        l, r = depth(node.left), depth(node.right)
        max_d[0] = max(max_d[0], l + r)
        return 1 + max(l, r)
    depth(root)
    return max_d[0]


# --- DFS: Max Path Sum ---
def max_path_sum(root: Optional[TreeNode]) -> int:
    best = [float('-inf')]
    def dfs(node):
        if not node: return 0
        l = max(dfs(node.left), 0)
        r = max(dfs(node.right), 0)
        best[0] = max(best[0], node.val + l + r)
        return node.val + max(l, r)
    dfs(root)
    return best[0]


# --- BFS: Level Order ---
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    queue, result = deque([root]), []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result


# --- Inorder (yields sorted order for BST) ---
def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    stack, curr = [], root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0: return curr.val
        curr = curr.right


# --- Invert Tree ---
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root: return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


if __name__ == "__main__":
    # Build: [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3
    assert level_order(root) == [[3], [9, 20], [15, 7]]
    assert diameter(root) == 3
    print("✅ All tree templates passed!")
