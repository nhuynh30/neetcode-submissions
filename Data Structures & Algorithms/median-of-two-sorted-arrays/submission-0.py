class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        if len(nums2) < len(nums1):
            A,B = B,A
        length = len(A) + len(B)
        half = length//2
        l,r = 0, len(A)-1
        even = length%2 == 0

        while True:
            i = l+(r-l)//2
            j = half-i-2
            Aleft = A[i] if i>=0 else float('-infinity')
            Aright = A[i+1] if (i+1) < len(A) else float('infinity')
            Bleft = B[j] if j>=0 else float('-infinity')
            Bright = B[j+1] if (j+1)<len(B) else float('infinity')

            if Aleft<=Bright and Bleft<=Aright:
                if not even:
                    return min(Bright, Aright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2.0
            else:
                if Aleft>Bright:
                    r=i-1
                else:
                    l=i+1
        
        return -1