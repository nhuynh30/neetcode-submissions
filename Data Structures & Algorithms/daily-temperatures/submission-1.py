class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0]*len(temperatures)
        stack = [0] * len(temperatures)
        for i in range(len(temperatures)):
            
            while stack and temperatures[i]>temperatures[stack[-1]]:
                index = stack.pop()
                arr[index] = i-index

            stack.append(i)


        return arr

