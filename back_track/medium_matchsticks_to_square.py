class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        match_stick_len = sum(matchsticks) // 4
        sides = [0]*4

        if match_stick_len != sum(matchsticks) / 4:
            return False
        matchsticks.sort(reverse=True)
        def dfs(i):
            if i == len(matchsticks):
                return True
           
            for j in range(4):
                if sides[j] + matchsticks[i] <= match_stick_len:
                    sides[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        
        return dfs(0)

