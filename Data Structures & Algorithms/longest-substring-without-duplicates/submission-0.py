class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ls = []
        res = 0
        for right in range(len(s)):
            while s[right] in ls:
                ls.pop(0)
                left+=1

            ls.append(s[right])
            res = max(res, right-left+1)
        return res
                