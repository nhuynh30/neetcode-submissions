class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dic = {}
        if len(s1)+len(s2) != len(s3):
            return False

        def dfs(a,b,c):
            if a>=len(s1) and b>=len(s2) and c>=len(s3):
                return True
            if (a,b) in dic:
                return dic[(a,b)]
            if a<len(s1) and b<len(s2) and s1[a]==s3[c] and s2[b]==s3[c]:
                dic[(a,b)] = dfs(a+1,b,c+1) or dfs(a,b+1,c+1)
            elif a<len(s1) and s1[a]==s3[c]:
                dic[(a,b)] =  dfs(a+1,b,c+1)
            elif b<len(s2) and s2[b]==s3[c]:
                dic[(a,b)] =  dfs(a,b+1,c+1)
            else:
                dic[(a,b)]= False

            return dic[(a,b)]

        return dfs(0,0,0)