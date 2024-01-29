class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pro = 1
        c = 0
        
        for i in nums:
            if(i==0):
                c+=1
            else:
                pro = pro * i
            
        for i in nums:
            if c>1:
                res.append(0)
            
            elif c == 0:
                res.append(int(pro/i))
            
            else:
                if i == 0:
                    res.append(pro)
                else:
                    res.append(0)                
            
        return res