class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = {0: 1}
        cnt = 0
        for n in nums:
            cnt += n
            diff = cnt - k
            res += prefixSum.get(diff,0)
            prefixSum[cnt] = prefixSum.get(cnt,0)+1
        return res

