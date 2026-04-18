class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        
        nums.sort()
        res=[]

        for i in range(len(nums)-2):
            
            if i>0 and nums[i]==nums[i-1]:
                continue

            j = i+1
            k = len(nums)-1
            
            
            
            while(j<k):
                sumVal = nums[i]+nums[j]+nums[k]
                if sumVal>0:
                    k-=1
                elif sumVal<0:
                    j+=1
                else: 
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while(nums[j]==nums[j-1] and j<k):
                        j+=1
                    while(nums[k]==nums[k+1] and j<k):
                        k-=1
            

        return res
