class Twitter:

    def __init__(self):
        self.followed = {}
        self.tweet = {}
        self.time = 0



    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweet:
            self.tweet[userId].append((-self.time, tweetId))
        else:
            self.tweet[userId] = [(-self.time, tweetId)]
        self.time+=1
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        lst = set()
        if userId in self.followed:
            lst = self.followed[userId].copy()
        lst.add(userId)

        k=0
        x = []
        for user in lst:
            for tweet in self.tweet.get(user,[]):
                heapq.heappush(x, tweet)
        
        res = []
        while len(res)<10 and x:
            time, tweetid = heapq.heappop(x)
            res.append(tweetid)
            k+=1
        
        return res

            


        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followed:
            self.followed[followerId].add(followeeId)
        else:
            self.followed[followerId] = set()
            self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followed:
            self.followed[followerId].discard(followeeId)
        
