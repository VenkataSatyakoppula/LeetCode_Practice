class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arrLen = len(nums)
        for i in range(arrLen):
            nums.append(nums[i])
        return nums
