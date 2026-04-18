class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = 1000000
        while l<=r:
            mid = l + (r-l)//2
            res = min(res, nums[mid])
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r=mid-1
        return res
            
                
                    
