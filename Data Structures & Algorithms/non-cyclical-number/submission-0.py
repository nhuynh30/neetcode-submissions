class Solution:
    def isHappy(self, n: int) -> bool:
        def compute(x):
            res = 0
            for i in str(x):
                res+= int(i)**2

            return res
        seen = set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            n = compute(n)

        return True

        
        