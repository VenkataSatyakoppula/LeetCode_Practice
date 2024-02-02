class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        res = []
        for i in nums:
            res.append(total)
            total *= i
        total =1
        for j in range(len(nums)-1,-1,-1):
            res[j] = total*res[j]
            total *= nums[j]
        return res
