class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0, len(nums) - 1
        i = 0
        def swap(i,j):
            nums[i] = nums[i]^nums[j]
            nums[j] = nums[i]^nums[j]
            nums[i] = nums[i]^nums[j]
        while(i <= r):
            if nums[i] == 0:
                if nums[i] != nums[l]:
                    swap(l,i)
                l +=1
            elif nums[i] == 2:
                if nums[i] != nums[r]:
                    swap(i,r)
                r -=1
                i -=1
            i +=1

