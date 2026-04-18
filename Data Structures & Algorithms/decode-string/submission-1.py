class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        string = ""
        num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                num= num*10 + int(s[i])
            elif s[i].isalpha():
                string+= s[i]
            elif s[i]=='[':
                stack.append((string, num))
                string = ""
                num=0
            elif s[i] == ']':
                prevStr, prevNum = stack.pop()
                string = prevStr + prevNum*string
        
        return string
