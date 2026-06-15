class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num2 = num2[::-1]
        num1 = num1[::-1]
        res = [0] * (len(num1)+len(num2))
        digit = 0
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                total = int(num1[i]) * int(num2[j])
                res[i+j] += total
                res[i+j+1] += (res[i+j] // 10)
                res[i+j] %= 10
                
        res = res[::-1]
    
        while len(res) >1 and res[0] == 0:
            res.pop(0)

        return "".join(str(x) for x in res)
