class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        def swap(l,r):
            t = s[l]
            s[l] = s[r]
            s[r] = t
        while(l <= r):
            swap(l,r)
            r -=1
            l +=1 

