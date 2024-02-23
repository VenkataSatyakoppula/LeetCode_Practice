class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(inp):
            l=0
            r = len(inp)-1
            while(l<=r):
                mid = (l+r)//2
                if inp[mid]<target:
                    l=mid+1
                elif inp[mid]>target:
                    r=mid-1
                else:
                    return True
            return False
        
        for mat in matrix:
            if (binary_search(mat)):
                return True
        return False
