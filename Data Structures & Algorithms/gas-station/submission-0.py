class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)< sum(cost):
            return -1

        diff = [0] * len(gas)
        for i in range(len(gas)):
            diff[i]= gas[i]-cost[i]
        
        for i in range(len(diff)):
            total = 0
            for j in range(len(diff)):
                index = (i+j)%len(diff)
                total+= diff[index]
                if total < 0:
                    break
            if total>=0:
                return i

        return -1