class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        target = total/4

        def dfs(i, sides):
            if i==len(matchsticks):
                return True

            seen = set()
            for j in range(len(sides)):
                if sides[j] in seen:
                    continue
                seen.add(sides[j])

                if sides[j]+matchsticks[i] <= target:
                    sides[j]+= matchsticks[i]
                    if dfs(i+1, sides):
                        return True
                    sides[j]-= matchsticks[i]

            return False

        
        return dfs(0,[0,0,0,0])