class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, curr, valsum):
            if valsum==target:
                res.append(curr[:])
                return
            if valsum>target:
                return
            
            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtrack(i, curr, valsum+nums[i])
                curr.pop()


        backtrack(0, [], 0)
        return res