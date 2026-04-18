class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0;
        res=1
        nums=set(nums)

        
        for num in nums:
            if num-1 not in nums:
                count = 0
                curr = num
                while (curr in nums):
                    count+=1
                    curr+=1

                res = max(res,count)
        return res