class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize !=0:
            return False
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n,0)
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            mini = minH[0]
            for i in range(mini,mini+groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

