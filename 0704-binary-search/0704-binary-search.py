class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l != r:
            m = l + ((r-l)//2)
            if target < nums[m]:
                r = m
            elif target > nums[m]:
                l = m+1
            elif nums[m] == target:
                return m
        return -1