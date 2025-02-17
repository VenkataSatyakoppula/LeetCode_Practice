class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        hashMap = {}
        for n in nums:
            hashMap[n] = hashMap.get(n,0) + 1
        
        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in hashMap:
                if hashMap[n] <= 0:
                    continue
                perm.append(n)
                hashMap[n] -= 1
                dfs(perm)
                hashMap[n] +=1
                perm.pop()
        
        dfs([])
        return res

