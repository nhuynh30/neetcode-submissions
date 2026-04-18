class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in range(len(asteroids)):
            while stack and (stack[-1]>0 and asteroids[i]<0):
                num1 = abs(stack[-1])
                num2 = abs(asteroids[i])
                if num1 > num2:
                    break
                elif num1<num2:
                    stack.pop()
                else:
                    stack.pop()
                    break
            else: 
                stack.append(asteroids[i])
                    
           
        return stack