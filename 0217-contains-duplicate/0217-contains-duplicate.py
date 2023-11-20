class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()

#         for i in range(0, len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return True
            
#         return False
        hashset = set()
        
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
                
        return False
        