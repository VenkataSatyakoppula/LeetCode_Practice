class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        l,r = 0, len(height)-1

        while(l<r):
            area = (r-l)*min(height[l],height[r])
            if height[l]<=height[r]:
                l +=1
            elif height[l]>height[r]:
                r -=1
            max_area = max(max_area,area)
        return max_area
