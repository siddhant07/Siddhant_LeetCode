class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        
        length = len(A) + len(B)
        
        half = length//2 if length%2==0 else (length+1)//2
        
        if len(A)>len(B):
            A,B = B,A
        
        l, r = 0, len(A) - 1
        
        while True:
            mA = (l+r)//2
            mB = half - mA - 2 
            lA = A[mA] if mA >= 0 else float("-infinity")
            lB = B[mB] if mB >= 0 else float("-infinity")
            rA = A[mA+1] if (mA+1)<len(A) else float("infinity")
            rB = B[mB+1] if (mB+1)<len(B) else float("infinity")
            
            if lB <= rA and lA <= rB:
                if length%2 == 0:
                    return (max(lA,lB) + min(rA,rB) )/2
                else:
                    return max(lA,lB)                

            elif lA > rB:
                r = mA - 1
            else:
                l = mA + 1
                
            
            
        