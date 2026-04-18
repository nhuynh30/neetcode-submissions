class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0;
        dic = {}
        res=0

        
        for num in nums:
            if num-1 not in nums:
                dic[num]=0
                curr = num
                while (curr in nums):
                    dic[num] +=1
                    curr+=1

            res = max(res,dic.get(num,1))
        return res