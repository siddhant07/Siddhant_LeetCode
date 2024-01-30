class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        res = [1] * (len(nums)-1)
        
        res.append(pre)
        
        for i in range(1, len(nums)):
            pre = pre * nums[i-1]
            res[i] = pre
            
            
        post = 1
        for i in range(len(nums) - 2, -1, -1):
            post = post * nums[i+1]
            res[i] = res[i] * post
            
        return res
        