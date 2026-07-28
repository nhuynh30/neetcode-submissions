class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(lst):
            if len(lst)==len(nums):
                res.append(lst[:])
                return
            for i in nums:
                if i not in lst:
                    lst.append(i)
                    dfs(lst)
                    lst.pop()

        dfs([])
        return res

