class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr, opencnt, closecnt):
            if len(curr)==2*n:
                res.append("".join(curr))
                return
            if opencnt<n:
                curr.append("(")
                dfs(curr,opencnt+1,closecnt)
                curr.pop()

            if closecnt<opencnt:
                curr.append(")")
                dfs(curr, opencnt, closecnt+1)
                curr.pop()

        dfs([],0,0)
        return res
            

            