class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        sumarr = 0
        for num in nums:
            if sumarr+num>num:
                sumarr+=num
            else:
                sumarr=num
            res = max(res, sumarr)
        return res