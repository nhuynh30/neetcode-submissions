class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatHour(x):
            hr = 0
            for i in range(len(piles)):
                if piles[i]<=x:
                    hr+=1
                else:
                    hr += math.ceil(piles[i]/x)

            return hr

        minhr = 1
        maxhr = max(piles)
        res = 0

        while minhr<maxhr:
            mid = minhr + (maxhr - minhr)//2
            hr = eatHour(mid)
            if hr>h:
                minhr = mid+1
            else:
                maxhr = mid

        return maxhr

        

