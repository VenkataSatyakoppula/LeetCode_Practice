class TrieNode:
    """A node in the Trie structure."""
    def __init__(self):
        self.children = {} 
        self.is_end_of_word = False

class Trie:
    """The Trie data structure."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Inserts a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Searches for a word in the Trie and returns True if found."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        cache = {len(s):0}
        for word in dictionary:
            trie.insert(word)
        
        def dfs(i):
            if i in cache:
                return cache[i]
            
            res = 1 + dfs(i+1)
            for j in range(i,len(s)):
                if trie.search(s[i:j+1]):
                    res = min(res,dfs(j+1))
            cache[i] = res
            return res
        return dfs(0)

