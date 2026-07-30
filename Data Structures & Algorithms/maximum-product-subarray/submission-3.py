class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[-9999, 9999] for _ in range(len(nums))]
        dp[0] = (nums[0],nums[0])
        res = -99999
        for i in range(1,len(nums)):
            dp[i][0] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
            dp[i][1] = min(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
            res = max(res, dp[i][0])
        return max(res, dp[-1][0])
