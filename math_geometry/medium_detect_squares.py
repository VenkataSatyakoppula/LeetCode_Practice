class DetectSquares:

    def __init__(self):
        self.points = []
        self.ptsmap = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.ptsmap[tuple(point)] +=1

    def count(self, point: List[int]) -> int:
        cnt =0
        a,b = point
        for x,y in self.points:
            if abs(x-a) != abs(y-b) or x==a or y==b:
                continue
            cnt += self.ptsmap[(a,y)]*self.ptsmap[(x,b)]
        
        return cnt
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
