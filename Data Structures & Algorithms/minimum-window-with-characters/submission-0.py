class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic1 = {}
        dic2= {}
        l = 0
        need = 0
        have = 0
        res = ""
        minLen = 10000

        for i in range(len(t)):
            if dic2.get(t[i],0) == 0:
                need +=1
            dic2[t[i]] = dic2.get(t[i], 0) +1

        for r in range(len(s)):
            char = s[r]
            dic1[s[r]] = dic1.get(s[r], 0)+1
            if dic1[s[r]] == dic2.get(s[r], 0):
                have+=1
            while have == need:
                if minLen > r-l+1:
                    minLen = r-l+1
                    res = s[l:r+1] 
                if dic1[s[l]] == dic2.get(s[l], 0):
                    have-=1
                dic1[s[l]]-=1
                l+=1    
                
        
        return res
        



        

        