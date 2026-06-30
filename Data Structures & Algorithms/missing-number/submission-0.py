class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = len(nums)
        b = 0
        for i in range(len(nums)):
            a ^= i
            b ^= nums[i]
        return a ^ b