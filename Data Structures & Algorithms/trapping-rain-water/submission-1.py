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
                minHeight = height[left]
                left+=1
            else:
                minHeight= height[right]
                right-=1
            water = min(leftMax, rightMax) - minHeight
            res += water if water > 0 else 0

        return res

            

            

            
            

            
            

        