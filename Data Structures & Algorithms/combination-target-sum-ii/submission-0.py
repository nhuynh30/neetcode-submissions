class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res=[]
        def backtrack(index, sumval, curr):
            if sumval==target:
                res.append(curr[:])
                return
            if sumval>target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                backtrack(i+1, sumval+candidates[i], curr)
                curr.pop()

        backtrack(0,0, [])

        return res