"""Tries — Reusable Templates"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end
    
    def starts_with(self, prefix: str) -> bool:
        return self._find(prefix) is not None
    
    def _find(self, prefix: str):
        node = self.root
        for c in prefix:
            if c not in node.children: return None
            node = node.children[c]
        return node


class WordDictionary:
    """LC #211 — Supports '.' wildcard matching."""
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word): return node.is_end
            if word[i] == '.':
                return any(dfs(child, i+1) for child in node.children.values())
            if word[i] not in node.children: return False
            return dfs(node.children[word[i]], i+1)
        return dfs(self.root, 0)


if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    assert t.search("apple") == True
    assert t.search("app") == False
    assert t.starts_with("app") == True
    
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    assert wd.search("b.d") == True
    assert wd.search("b..") == True
    print("✅ All trie templates passed!")
