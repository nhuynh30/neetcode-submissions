class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(i, lst):
            if i >len(nums):
                return

            ans.append(lst[:])
            for j in range(i, len(nums)):
                lst.append(nums[j])
                backtrack(j+1, lst)
                lst.pop()
            

        
        
        backtrack(0, [])
        return ans