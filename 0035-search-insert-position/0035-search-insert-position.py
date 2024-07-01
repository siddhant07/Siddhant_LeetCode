class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, m, r = 0, 0, len(nums)
        
        while l!=r:
            m = (l+r)//2
            
            if nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m+1
            elif nums[m] == target:
                return m
        return l
        