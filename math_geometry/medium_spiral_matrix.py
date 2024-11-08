class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        N = len(matrix[0])
        res = []
        l,r=0,0
        while(len(res) < M*N):
            # Go right
            while(r<N and matrix[l][r] != -10000):
                res.append(matrix[l][r])
                matrix[l][r] = -10000
                r +=1
            r -=1
            l +=1
            #Go Down
            while(l<M and matrix[l][r] != -10000):
                res.append(matrix[l][r])
                matrix[l][r] = -10000
                l +=1
            l -=1
            r -=1
            
            #Go left
            while(r>0 and matrix[l][r] != -10000):
                res.append(matrix[l][r])
                matrix[l][r] = -10000
                r-=1
            if(matrix[l][r] == -10000):
                l-= 1
                r += 1
            #Go Top
            while(l>0 and matrix[l][r] != -10000):
                res.append(matrix[l][r])
                matrix[l][r] = -10000
                l -= 1
            l +=1
            r +=1

        return res

