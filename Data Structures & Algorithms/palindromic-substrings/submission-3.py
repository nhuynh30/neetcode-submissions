class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindrome(s):
            res = 0

            for i in range(len(s)):
                res+=1
                l=i-1
                r=i+1
                if l<0 or r>=len(s):
                    continue
                
                while l>=0 and r<len(s) and s[l]==s[r]:
                    res+=1
                    l-=1
                    r+=1
                
                else:
                    continue

            
            for i in range(len(s)):
                l=i
                r=i+1
                
                if l<0 or r>=len(s):
                    continue
                
                while l>=0 and r<len(s) and s[l]==s[r]:
                    res+=1
                    l-=1
                    r+=1
                else:
                    continue

            return res

        return countPalindrome(s)
                
