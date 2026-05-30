class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        dic = {}
        hand.sort()
        for i in hand:
            dic[i] = dic.get(i,0)+1
        
        smallest = hand[0]
        while dic:
            for i in range(smallest, smallest+groupSize):
                if i not in dic:
                    return False
                dic[i]-=1
                if dic[i]==0:
                    del dic[i]
            if dic:
                smallest = min(dic.keys())
        
        return True

