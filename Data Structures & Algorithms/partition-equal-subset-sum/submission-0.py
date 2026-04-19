class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums)):
            nextDP = set()
            for num in dp:
                nextDP.add(num+nums[i])
                nextDP.add(num)
            dp = nextDP
        return True if target in dp else False