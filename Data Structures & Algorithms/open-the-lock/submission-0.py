class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        queue.append(("0000",0))
        if "0000" == target:
            return 0
        dead = set(deadends)
        if "0000" in dead:
            return -1
        visited = set()

        while queue:
            num,step = queue.popleft()
            step+=1
            for i in range(len(num)):
                digit1 = (int(num[i]) + 1)%10
                digit2 = (int(num[i]) - 1 )%10

                num1 = num[:i] + str(digit1) + num[i+1:]
                num2 = num[:i] + str(digit2) + num[i+1:]

                if num1 not in visited and num1 not in dead:
                    if num1 == target:
                        return step
                    visited.add(num1)
                    queue.append((num1, step))

                if num2 not in visited and num2 not in dead:
                    if num2 == target:
                        return step
                    visited.add(num2)
                    queue.append((num2, step))

        return -1


