#Review again 
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False
        s1_map = [0]*26
        s2_map = [0]*26
        for i in range(len(s1)):
            s1_map[ord(s1[i])-ord('a')] +=1 
            s2_map[ord(s2[i])-ord('a')] +=1
        matches = 0
        for i in range(26):
            if s1_map[i] == s2_map[i]:
                matches +=1
        l = 0
        for i in range(len(s1),len(s2)):
            if matches==26:
                return True
            index = ord(s2[i]) - ord('a')
            s2_map[index] += 1
            if s2_map[index] == s1_map[index]:
                matches +=1
            elif s1_map[index]+1 == s2_map[index]:
                matches -=1
            index = ord(s2[l]) - ord('a')
            s2_map[index] -= 1
            if s2_map[index] == s1_map[index]:
                matches +=1
            elif s1_map[index]-1 == s2_map[index]:
                matches -=1
            l +=1

        return matches == 26
        
