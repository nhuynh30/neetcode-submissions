class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort(reverse=True)
        l,r=0, len(people)-1
        while l<=r:
            total = people[l] + people[r]
            if total > limit:
                res+=1
                l+=1
            elif total <= limit:
                l+=1
                r-=1
                res+=1

        return res