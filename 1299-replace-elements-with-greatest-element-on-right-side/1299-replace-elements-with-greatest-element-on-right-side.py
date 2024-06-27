class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        for i in range(len(arr)-1 , -1 , -1):            
            res[i - 1] = max(arr[i], res[i])
        
        res[-1] = -1
        
        return res
            
        