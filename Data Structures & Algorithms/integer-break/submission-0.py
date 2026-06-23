class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(2,n+1):
            for j in range(2, i):
                num = max(dp[j], j) * max(dp[i-j], i-j)
                dp[i] = max(dp[i], num)

        return dp[n] 