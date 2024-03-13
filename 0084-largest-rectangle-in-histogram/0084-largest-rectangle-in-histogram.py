class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxAr= 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                j, xh = stack.pop()
                maxAr = max(maxAr, (i-j)*xh)
                start = j
            stack.append((start ,h))
            
        for i, h in stack:
            maxAr = max(maxAr, (len(heights)-i)*h)
        
        return maxAr
                
                
        