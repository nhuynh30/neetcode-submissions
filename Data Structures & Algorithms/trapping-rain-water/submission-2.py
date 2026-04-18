class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        leftMax = 0
        rightMax = 0
        res = 0
        while left<right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if height[left]<height[right]:
                water = leftMax-height[left]
                left+=1
            else:
                water= rightMax - height[right]
                right-=1
            
            res += water if water > 0 else 0

        return res
            

            

            
            

            
            

        