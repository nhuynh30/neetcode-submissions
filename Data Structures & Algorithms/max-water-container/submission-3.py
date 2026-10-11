class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        ans = 0
        while left<right:
            h = min(heights[left],heights[right])
            w = right-left
            ans = max(ans, h*w)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1

        return ans