class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1]*2 for _ in range(len(prices))]
        def dfs(i, holding):
            if i>= len(prices):
                return 0
            if holding:
                if dp[i][0] != -1:
                    return dp[i][0]
                sell = prices[i] + dfs(i+2, False)
                hold = dfs(i+1, True)
                dp[i][0] = max(sell,hold)
                return dp[i][0]
            else:
                if dp[i][1] != -1:
                    return dp[i][1]
                buy = dfs(i+1, True) - prices[i]
                skip = dfs(i+1, False)
                dp[i][1] = max(buy, skip)
                return dp[i][1]

        return dfs(0, False)

        
