class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ls = set()
        for i in range(len(nums)):
            if nums[i] not in ls:
                ls.add(nums[i])
            else:
                return True
        
        return False