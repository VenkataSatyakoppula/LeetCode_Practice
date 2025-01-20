class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        h_map = defaultdict(int)
        for i in range(len(nums)):
            h_map[nums[i]] += 1
            if len(h_map) <=2:
                continue
            new_map = defaultdict(int)
            for n , c in h_map.items():
                if c > 1:
                    new_map[n] = c-1
            h_map = new_map
        
        for key in h_map:
            if nums.count(key) > len(nums) // 3:
                res.append(key)
        return res

