class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {} , {}
        l = 0
        for ele in t:
            countT[ele] = 1 + countT.get(ele,0)
        
        have, need = 0, len(countT)
        res, resLen = [-1,-1] , float("infinity")
        for i in range(len(s)):

            window[s[i]] = 1 + window.get(s[i],0)
            if s[i] in countT and window[s[i]] == countT[s[i]]:
                have +=1
            while(have == need):
                if(i-l+1 < resLen):
                    resLen = i-l+1
                    res = [l,i]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l +=1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""

