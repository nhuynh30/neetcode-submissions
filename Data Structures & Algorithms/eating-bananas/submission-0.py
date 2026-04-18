from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkHour(k):
            totalHr = 0
            for i in piles:
                totalHr += ceil(float(i)/k)
            
            return totalHr

        l = 1
        r = max(piles)
        res = 10000000000

        while(l<=r):
            mid = l+(r-l)//2
            totalHr = checkHour(mid)
            if totalHr>h:
                l=mid+1
            else:
                r=mid-1
                res = min(res, mid)

        return res
