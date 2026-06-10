class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dic = {}
        def dfs(i,j):
            if (i,j) in dic:
                return dic[(i,j)]
            if i>=len(word1):
                dic[(i,j)] = len(word2)-j
            elif j>=len(word2):
                dic[(i,j)] = len(word1)-i
            elif word1[i]==word2[j]:
                dic[(i,j)] = dfs(i+1,j+1)
            elif word1[i] != word2[j]:
                insert = dfs(i, j+1)
                delete = dfs(i+1, j)
                replace = dfs(i+1, j+1)
                dic[(i,j)] = 1 + min(insert, delete, replace)

            return dic[(i,j)]

        return dfs(0,0)