class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = 0
        flag = 0
        for i in range(len(matrix)):
            if target <= matrix [i][-1]:
                lst = i
                flag = 1
                break
                
        if flag == 0:
            return False
        
        l = 0
        r = len(matrix[lst])
        
        while l!= r:
            m = l + ((r-l)//2)
            if target < matrix[lst][m]:
                r = m
            elif target > matrix[lst][m]:
                l = m+1
            elif target == matrix[lst][m]:
                return True
        
        return 0
    
            
        
        
                
        