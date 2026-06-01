class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0
        for i in s:
            if i=="(":
                min_open+=1
                max_open+=1
            elif i=="*":
                max_open+=1
                min_open-=1
            else:
                min_open-=1
                max_open-=1
            
            if max_open<0:
                return False
            if min_open<0:
                min_open=0

        return min_open==0 