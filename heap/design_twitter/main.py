"""
https://neetcode.io/problems/design-twitter-feed/question?list=neetcode150

Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.

Users and tweets are uniquely identified by their IDs (integers).

Implement the following methods:

    Twitter() Initializes the twitter object.
    void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
    list<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.
    void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
    void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.
"""

NUM_MOST_RECENT_TWEETS = 10

import heapq

class User:
    def __init__(self, userId: int):
        # min-heap
        self.userId = userId

        # Array of (timestamp, tweetId, userId) tuples
        self.feed = []

        # Users follow themselves
        self.followers = set([userId])

        # People this user follows
        self.followees = set([userId])

        self.stored_tweet_ids = set()

        # Tweets this user has made
        self.own_tweets = set()

    def __repr__(self):
        return f"""\n(userId: {self.userId}, feed: {self.feed}, followers: {self.followers}, followees: {self.followees})\n"""

    def sendOwnTweetsToNewFollower(self, follower: "User"):
        for tweet in self.own_tweets:
            follower.addTweet(tweet)

    """
    Where tweet is a tuple (timestamp, tweetId, userId)
    and userId is the id of the user who made the post
    """
    def addTweet(self, tweet: tuple[int,int,int]):
        _,tweetId,userId = tweet

        # An extra check to make sure we only add tweets of
        # people that we follow
        if userId in self.followees and tweetId not in self.stored_tweet_ids:
            heapq.heappush(self.feed, tweet)
            self.stored_tweet_ids.add(tweetId)

    def publishTweetToFollowers(self, tweet: tuple[int,int,int], user_map):
        #print(f"Publish tweet {tweet} to all followers of user {self.userId}...")
        self.own_tweets.add(tweet)
        for follower_id in self.followers:
            if follower_id not in user_map:
                raise Exception(f"userId {follower_id} not in self.user_map")

            follower = user_map[follower_id]
            follower.addTweet(tweet)

    def addFollowee(self, userId: int):
        self.followees.add(userId)

    def removeFollowee(self, userId: int):
        if userId in self.followees:
            self.followees.remove(userId) 

    def addFollower(self, userId: int):
        self.followers.add(userId)

    def removeFollower(self, userId: int):
        if userId in self.followers:
            self.followers.remove(userId)

    """
    Pops most recent values from feed
    """
    def getFeed(self, n: int):
        res = []

        while len(res) < n and self.feed:
            tweet = heapq.heappop(self.feed)
            _, tweetId, userId = tweet

            # Lazily discard tweets of users we don't follow
            # If the user has stopped following the person we discard their tweet 
            # During this process without eagerly looking it up and discarding
            if userId in self.followees:
                res.append(tweet)
            # else tweet is discarded in next iteration


            # Always remove stored tweet id, because it will just be added
            # back anyway
            self.stored_tweet_ids.remove(tweetId)

        return res

class Twitter:

    def __init__(self):
        
        # Global time counter
        self.timestamp = 0

        # keys = userId's
        # vals = User class
        self.user_map = {}

    def createNewUser(self, userId):
        #print(f"Creating new user with id {userId}")
        user = User(userId)
        self.user_map[userId] = user
        return user

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_map:
            self.createNewUser(userId)

        user = self.user_map[userId]
        new_tweet = (self.timestamp, tweetId, userId)
        user.publishTweetToFollowers(new_tweet, self.user_map)
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
#        if userId not in self.user_map:
#            raise Exception(f"userId {userId} not in self.user_map")
        if userId not in self.user_map:
            self.createNewUser(userId)

        user: User = self.user_map[userId]

        res = []
        feed = user.getFeed(NUM_MOST_RECENT_TWEETS)

        for tweet in feed:
            res.append(tweet[1])
            user.addTweet(tweet)

        return res

    def __repr__(self):
        return f"{self.user_map}"
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_map:
            self.createNewUser(followerId)
        if followeeId not in self.user_map:
            self.createNewUser(followeeId)

        follower, followee = self.user_map[followerId], self.user_map[followeeId]

        if followerId in followee.followers and followeeId in follower.followees:
            return

        follower.addFollowee(followeeId)
        followee.addFollower(followerId)

        # Send all tweets that you have made to the new follower
        followee.sendOwnTweetsToNewFollower(follower)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_map:
            self.createNewUser(followerId)
        if followeeId not in self.user_map:
            self.createNewUser(followeeId)

        follower, followee = self.user_map[followerId], self.user_map[followeeId]

        if followerId not in followee.followers and followeeId not in follower.followees:
            return

        follower.removeFollowee(followeeId)
        followee.removeFollower(followerId)
        
twitter = Twitter()


twitter.postTweet(1,1)
twitter.postTweet(1,2)
twitter.postTweet(1,3)
twitter.postTweet(1,4)
twitter.postTweet(1,5)
twitter.postTweet(2,6)
twitter.postTweet(2,7)
twitter.follow(1,2)
print(twitter.getNewsFeed(1))

#print(twitter)

