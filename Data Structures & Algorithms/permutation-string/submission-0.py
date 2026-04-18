class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1 = sorted(s1)
        current = []

        if len(s1)>len(s2):
            return False

        for i in range(k):
            current.append(s2[i])
            if sorted(current) == s1:
                return True
        
        for i in range(k, len(s2)):
            current.pop(0)
            current.append(s2[i])
            if sorted(current) == s1:
                return True

        return False


