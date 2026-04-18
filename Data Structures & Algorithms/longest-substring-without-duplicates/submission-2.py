class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ls = set()
        res = 0
        for right in range(len(s)):
            while s[right] in ls:
                ls.remove(s[left])
                left+=1

            ls.add(s[right])
            res = max(res, right-left+1)
        return res
                