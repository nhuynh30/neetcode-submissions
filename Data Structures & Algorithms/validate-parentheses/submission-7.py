class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for i in s:
            if i in dic.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                
                remove = stack.pop()
                if remove != dic[i]:
                    return False
        
        return False if stack else True
