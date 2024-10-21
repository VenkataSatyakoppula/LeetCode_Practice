class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dif = []
        index = 0
        total = 0
        for i in range(len(gas)):
            dif.append(gas[i] - cost[i])
            total += dif[i]
            if total < 0:
                total = 0
                index = i+1
        
        if sum(dif)<0:
            return -1
        return index
