class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        maxFreq = 0
        left = 0
        res=0

        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right],0)+1

            windowSize = right-left+1
            while windowSize-max(dic.values())>k:
                dic[s[left]]-=1
                left+=1
                windowSize = right-left+1
            
            res = max(res, right-left+1)
        
        return res
