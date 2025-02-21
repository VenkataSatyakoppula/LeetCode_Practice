class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        nums.sort(reverse=True)
        target = total // k
        n = len(nums)

        def backtrack(i, k, subsetSum, mask):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k - 1, 0, mask)
            for j in range(i, n):
                if (mask & (1 << j)) == 0 or subsetSum + nums[j] > target:
                    continue
                if backtrack(j + 1, k, subsetSum + nums[j], mask ^ (1 << j)):
                    return True
                if subsetSum == 0:
                    return False
            return False

        return backtrack(0, k, 0, (1 << n) - 1)
