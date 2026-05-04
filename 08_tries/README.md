# Tries

## 🎯 When to Use
**Signal words**: "prefix", "autocomplete", "starts with", "word dictionary", "word search"

## 📐 Template
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
    
    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_end
    
    def starts_with(self, prefix):
        return self._find(prefix) is not None
    
    def _find(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children: return None
            node = node.children[c]
        return node
```

## 🏋️ Practice Problems
| # | Problem | Difficulty | Key Insight |
|---|---------|-----------|-------------|
| 1 | LC #208 Implement Trie | Medium | Core template above |
| 2 | LC #211 Add and Search Word | Medium | Trie + DFS for '.' wildcards |
| 3 | LC #212 Word Search II | Hard | Trie + Backtracking on grid |
| 4 | LC #139 Word Break | Medium | DP + Trie for efficient prefix checking |
