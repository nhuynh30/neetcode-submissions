class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkpalindrome(l,r):
            if l<0 or r>=len(s):
                return s[l+1:r]
            
            if s[l]==s[r]:
                return checkpalindrome(l-1,r+1)
            else:
                return s[l+1:r]

        res = ""
        for i in range(len(s)):
            odd = checkpalindrome(i,i)
            even = checkpalindrome(i,i+1)
            if len(odd)>len(res):
                res=odd
            if len(even)>len(res):
                res=even

        return res