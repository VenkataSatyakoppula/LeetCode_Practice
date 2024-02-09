class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        h_map = {}
        l=0
        res =0
        max_ref = 0
        for r in range(len(s)):
            h_map[s[r]] = 1 + h_map.get(s[r],0)
            max_ref = max(max_ref,h_map[s[r]])
            if (r-l+1)-max_ref>k:
                h_map[s[l]] -=1
                l +=1
            res = max(res,r-l+1)
        return res
