class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = max(nums)
        right = sum(nums)
        res=1000000001
        def check(num):
            count = 1
            x = num
            for i in nums:
                if x-i>=0:
                    x-=i
                else:
                    count+=1
                    x=num-i
            return count
        while left<=right:
            mid = left + (right-left)//2
            x=check(mid)
            if x>k:
                left = mid+1
            else:
                res = min(res, mid)
                right=mid-1
        return res
