class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        arr = [0] * len(position)
        for i in range(len(position)):
            arr[i] = (position[i], speed[i])

        arr = sorted(arr, reverse = True)
        ans = 1
        for i in range(len(arr)):
            time = (target-arr[i][0])/float(arr[i][1])
            if len(stack)==0:
                stack.append(time)
            elif stack[-1]>=time:
                continue
            else:
                ans+=1
                stack.append(time)

        return ans


        
