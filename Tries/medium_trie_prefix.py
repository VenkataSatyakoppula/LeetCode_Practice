class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.trie = TrieNode()        

    def insert(self, word: str) -> None:
        itr = self.trie
        for c in word:
            if c not in itr.children:
                itr.children[c] = TrieNode()
            itr = itr.children[c]
        itr.endOfWord = True
        

    def search(self, word: str) -> bool:
        itr = self.trie
        for c in word:
            if c not in itr.children:
                return False
            itr = itr.children[c]
        
        return itr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        itr = self.trie
        for c in prefix:
            if c not in itr.children:
                return False
            itr = itr.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
