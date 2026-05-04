# Trees

## 🎯 When to Use This Pattern
**Signal words**: "binary tree", "BST", "depth", "path sum", "lowest common ancestor", "validate", "level order", "serialize"

## 🧠 Core Decision
- **Need level-by-level?** → BFS (Queue)
- **Need path/depth/subtree?** → DFS (Recursion)
- **Search/validate BST?** → Use BST property: left < node < right

## 📐 Templates

### DFS Template (Most tree problems)
```python
def dfs(node):
    if not node: return BASE_VALUE
    left = dfs(node.left)
    right = dfs(node.right)
    return COMBINE(node.val, left, right)
```

### BFS Template (Level-order)
```python
from collections import deque
def bfs(root):
    if not root: return []
    queue = deque([root])
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

## DFS Return Patterns
| Return Type | Example Problems |
|-------------|-----------------|
| Boolean | Validate BST, Same Tree, Symmetric |
| Integer | Max Depth, Diameter, Path Sum |
| Node | LCA, Inorder Successor |
| List | All Paths, Boundary |

## 🏋️ Practice Problems
| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #104 Maximum Depth | Easy | DFS returns 1 + max(left, right) |
| 2 | LC #226 Invert Binary Tree | Easy | Swap children, recurse |
| 3 | LC #100 Same Tree | Easy | Compare node values recursively |
| 4 | LC #102 Level Order Traversal | Medium | BFS with level tracking |
| 5 | LC #98 Validate BST | Medium | Pass min/max bounds down |
| 6 | LC #235 LCA of BST | Medium | Use BST property to navigate |
| 7 | LC #236 LCA of Binary Tree | Medium | DFS: return node if found in subtree |
| 8 | LC #543 Diameter of Binary Tree | Medium | DFS depth, track global max |
| 9 | LC #230 Kth Smallest in BST | Medium | Inorder traversal = sorted |
| 10 | LC #105 Construct from Pre+In | Medium | Preorder[0]=root, split inorder |
| 11 | LC #124 Binary Tree Max Path Sum | Hard | DFS returns max single-path, track global |
| 12 | LC #297 Serialize/Deserialize | Hard | BFS or preorder DFS |
