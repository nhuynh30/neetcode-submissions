class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic = {}
        self.res = 0
        def dfs(i, total):
            if i>=len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i, total) in dic:
                return dic[(i,total)]
            ways = dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])
            dic[(i, total)] = ways
            return ways
            
            
            

            
            

        return dfs(0, 0)
        



            