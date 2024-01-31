class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        
        for i,a in enumerate(nums):
            if a == nums[i-1] and i>0:
                continue
            
            else:
                l=i+1
                r=len(nums)-1
                while(l<r):
                    if(nums[l]+nums[r]+nums[i] == 0):
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l<r:
                            l += 1
                    elif (nums[l] + nums[r] + nums[i] < 0):
                        l += 1
                    else:
                        r -=1
            
        return res