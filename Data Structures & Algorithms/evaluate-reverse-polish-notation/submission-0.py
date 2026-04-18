class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+-/*':
                stack.append(int(i))
            else:
                num2= stack.pop()
                num1= stack.pop()
                if i== '+':
                    ans = num2+num1
                elif i== '-':
                    ans = num1-num2
                elif i== '/':
                    ans = int(num1/num2)
                else:
                    ans = num1 * num2
                stack.append(ans)
        
        return stack[0]

        