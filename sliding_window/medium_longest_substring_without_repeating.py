class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_cnt = 0
        l=0
        t =set()
        for i in range(len(s)):
            while (s[i] in t):
                t.remove(s[l])
                l +=1
            t.add(s[i])
            max_cnt = max(max_cnt,i-l+1)
        return max_cnt
