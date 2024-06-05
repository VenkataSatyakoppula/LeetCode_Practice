import heapq
class Twitter(object):

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.follos = defaultdict(set)
        
    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets[userId].append([self.count,tweetId])
        self.count -=1
        
    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res = []
        minHeap = []
        self.follos[userId].add(userId)
        for follower in self.follos[userId]:
            if follower in self.tweets:
                index = len(self.tweets[follower]) -1
                count, tweetId = self.tweets[follower][index]
                minHeap.append([count,tweetId,follower,index-1])
        heapq.heapify(minHeap)
        while minHeap and len(res)<10:
            count,tweetId,follower,index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index>=0:
                count,tweetId = self.tweets[follower][index]
                heapq.heappush(minHeap,[count,tweetId,follower,index-1])
        return res


    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follos[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.follos[followerId]:
            self.follos[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
