class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hmap = {}
        for i,w in enumerate(order):
            hmap[w] = i
        def comp(word1,word2):
            min_len = min(len(word1),len(word2))
            for i in range(min_len):
                if hmap[word1[i]] < hmap[word2[i]]:
                    return True
                elif hmap[word1[i]] > hmap[word2[i]]:
                    return False
            if word1[min_len-1] == word2[min_len-1] and len(word1) <= len(word2):
                return True
            return False 
        for i in range(len(words)-1):
            if not comp(words[i],words[i+1]):
                return False
        return True
