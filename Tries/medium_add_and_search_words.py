class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfword = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        
    def addWord(self, word: str) -> None:
        itr = self.trie
        for c in word:
            if c not in itr.children:
                itr.children[c] = TrieNode()
            itr = itr.children[c]
        itr.endOfword = True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            itr = root
            for i in range(j,len(word)):
                c = word[i]
                if c not in itr.children and c != '.':
                    return False
                if c == '.':
                    for child in itr.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    itr = itr.children[c]
            return itr.endOfword
        return dfs(0,self.trie)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
