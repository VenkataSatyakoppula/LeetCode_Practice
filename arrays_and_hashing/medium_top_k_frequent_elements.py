from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = {}
        for num in nums:
            if not num in h_map:
                h_map[num] = 1
            else:
                h_map[num] +=1
        
        sorted_vals = sorted(h_map.items(), key = lambda x:x[1],reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_vals[i][0])
        return res
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

if __name__ == "__main__":
    a = Solution()
    print(a.topKFrequent([1,1,1,2,2,3],2))
    print(a.topKFrequent2([1,1,1,2,2,3],2))
