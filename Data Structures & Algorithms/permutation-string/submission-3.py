class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = {}
        dic2 = {}
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            dic1[s1[i]] = dic1.get(s1[i], 0)+1
            dic2[s2[i]] = dic2.get(s2[i], 0)+1

        if dic1==dic2:
            return True
        for i in range(len(s1), len(s2)):
            remove = s2[i-len(s1)]
            dic2[remove] -=1
            if dic2[remove]==0:
                del dic2[remove]
            dic2[s2[i]] = dic2.get(s2[i],0)+1
            if dic1==dic2:
                return True


        return False

        
        
