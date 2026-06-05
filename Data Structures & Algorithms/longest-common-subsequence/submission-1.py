class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * len(text2) for _ in range(len(text1))]
        
        
        def dfs(i,j):
            if i>=len(text1) or j >= len(text2):
                return 0
            elif dp[i][j] != -1:
                return dp[i][j]

            elif text1[i]==text2[j]:
                dp[i][j]= 1 + dfs(i+1,j+1)

            else:
                left = dfs(i+1,j)
                right = dfs(i, j+1)
                dp[i][j] = max(left, right)

            return dp[i][j]

        return dfs(0,0)
            
