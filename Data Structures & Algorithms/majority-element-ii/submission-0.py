class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = 0,0
        cnt1, cnt2 = 0,0
        for num in nums:
            if num == cand1:
                cnt1+=1
            elif num==cand2:
                cnt2+=1
            elif cnt1==0:
                cand1=num
                cnt1=1
            elif cnt2==0:
                cand2=num
                cnt2=1
            else:
                cnt1-=1
                cnt2-=1
        
        cnt1,cnt2=0,0
        for num in nums:
            if num==cand1:
                cnt1+=1
            if num==cand2:
                cnt2+=1
        res=[]
        if cnt1> len(nums)//3:
            res.append(cand1)
        if cnt2> len(nums)//3:
            res.append(cand2)

        return res