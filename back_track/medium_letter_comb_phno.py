class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_map = {
            "2": ['a','b','c'],
            "3": ['d','e','f'],
            "4": ['g','h','i'],
            "5": ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['p','q','r','s'],
            "8": ['t','u','v'],
            "9": ['w','x','y','z']
        }
        res = []
        part= []
        if not digits:
            return []

        def dfs(i):
            if i>= len(digits):
                res.append(''.join(part))
                return 
            digi = number_map[digits[i]]
            for j in range(len(digi)):
                part.append(digi[j])
                dfs(i+1)
                part.pop()
        dfs(0)
        return res
