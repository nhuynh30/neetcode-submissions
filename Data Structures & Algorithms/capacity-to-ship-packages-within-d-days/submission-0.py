class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left = max(weights)
        right = sum(weights)
        res = 25000001
        def doable(mid):
            count =1
            m = mid
            for i in weights:
                if m-i>=0:
                    m-=i
                else:
                    count+=1
                    m=mid-i
            return count
        while left<=right:
            mid = left + (right-left)//2
            day = doable(mid)
            if day>days:
                left=mid+1
            else:
                right=mid-1
                res = min(res, mid)
        
        return res if res!=25000001 else 0

        