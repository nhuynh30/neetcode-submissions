class Solution:
    def longestPalindrome(self, s: str) -> str:
        odd = {}
        even = {}

        maxodd = ""
        for i in range(len(s)):
            l=i
            r=i
            while (l<=r and l>=0 and r<len(s)):
                if s[l]==s[r]:
                    l-=1
                    r+=1
                else:
                    break
            
            odd[i] = s[l+1:r]
            if len(odd[i]) > len(maxodd):
                maxodd = odd[i]


        maxeven = ""
        for i in range(1, len(s)):
            l=i-1
            r=i

            if (s[l]!=s[r]):
                even[i] = s[l:r+1]
                continue

            while (l<=r and l>=0 and r<len(s)):
                if s[l]==s[r]:
                    l-=1
                    r+=1
                else:
                    break

            even[i] = s[l+1:r]
            if len(maxeven) < len(even[i]):
                maxeven = even[i]

        if len(maxodd) >= len(maxeven):
            return maxodd;
        else:
            return maxeven
        

    


        

        

                

                


