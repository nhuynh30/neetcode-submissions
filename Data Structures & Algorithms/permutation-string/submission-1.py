class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        check = {}
        k = len(s1)
        count =0

        if len(s1) > len(s2):
            return False
        
        for i in range(k):
            dic[s1[i]] = dic.get(s1[i], 0) +1

        for i in range(k):
            check[s2[i]] = check.get(s2[i], 0) +1

        if check==dic:
            return True
        
        for i in range(k, len(s2)):
            check[s2[i-k]] -=1
            if check[s2[i-k]] == 0:
                del check[s2[i-k]]
            check[s2[i]] = check.get(s2[i], 0) +1
            if check == dic:
                return True

        return False

            
        