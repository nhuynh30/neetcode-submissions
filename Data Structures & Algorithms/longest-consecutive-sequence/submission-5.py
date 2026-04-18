class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        res = 1
        nums.sort()
        prev=100000
        
        if len(nums)==0:
            return 0
        for num in nums:
            if num==prev:
                continue
            prev=num
            if num-1 not in nums:
                dic[num] = dic.get(num,0)+1
            else:
                dic[num] = dic[num-1]+1
            
            res = max(res, dic[num])
        return res
