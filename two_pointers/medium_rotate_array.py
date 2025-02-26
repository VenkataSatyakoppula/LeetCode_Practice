class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        nums.reverse()
        l , r = 0, k - 1
        #Reverse left
        while (l<r):
            nums[l] , nums[r] = nums[r] , nums[l]
            l +=1
            r -=1
        #Reverse Right
        l , r = k, len(nums) -1
        while (l<r):
            nums[l] , nums[r] = nums[r] , nums[l]
            l +=1
            r -=1

