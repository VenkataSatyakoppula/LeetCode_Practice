from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        res = []
        h_map = {}
        for word in strs:
            h_word = str(sorted(word))
            
            if h_word not in h_map:
                h_map[h_word] = [word]
            else:
                h_map[h_word].append(word)
        for key in h_map:
            res.append(h_map[key])
        return res
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        h_map = defaultdict(list)

        for word in strs:
            chars = [0]*26
            for c in word:
                chars[ord(c)-ord("a")] += 1 
            h_map[tuple(chars)].append(word) 
        return h_map.values()

if __name__ == "__main__":
    a = Solution()
    print(a.groupAnagrams1(["eat","tea","tan","ate","nat","bat"]))
    print(a.groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))

