class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0+nums[0]
        for i in range(1, len(nums)):
            if farthest>=i:
                farthest = max(farthest, i + nums[i])

        return farthest >= len(nums)-1