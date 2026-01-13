class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        c = 0
        ans = 0
        while i<len(nums):
            if nums[i] == 1:
                c += 1
            else:
                ans = max(ans,c)
                c = 0
            ans = max(ans,c)
            i += 1

        return ans
        