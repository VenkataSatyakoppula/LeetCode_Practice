class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # h_map = {} time = O(n) space = O(n)
        # for num in nums:
        #     h_map[num] = 1 + h_map.get(num,0)
        # cnt =len(nums) // 2
        # for h in h_map:
        #     if h_map[h] > cnt:
        #         return h
        cnt = 0 # O(1) space
        res = 0
        for num in nums:
            if cnt ==0:
                res = num

            if res == num:
                cnt += 1
            else:
                cnt -= 1
        return res 

