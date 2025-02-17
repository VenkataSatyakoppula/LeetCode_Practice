class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(index,cur_xor):
            if index == len(nums):
                return cur_xor
            
            include = dfs(index+1,cur_xor^nums[index])
            exclude = dfs(index+1,cur_xor)
            return include+exclude
        
        return dfs(0,0)
