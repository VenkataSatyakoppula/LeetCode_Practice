class Solution(object):
    def isPalindrome(self, s):

        length = len(s)
        final_str = ""
        for i in range(length):
            if ((ord(s[i].lower())>=97 and ord(s[i].lower())<=122 ) or (ord(s[i])>=48 and ord(s[i])<=57)):
                final_str += s[i].lower()
        start =0 
        end = len(final_str) - 1
        
        if(len(final_str)==0):
            return True
        while(start < end):
            if not (final_str[start]==final_str[end]):
                return False
            start +=1
            end -=1    
        return True

