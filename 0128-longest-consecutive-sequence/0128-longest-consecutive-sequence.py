class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        longest = 0
        length = 0
        
        for i in nums:
            if (i-1) not in numset:
                length = 0
                while((i+length) in numset):
                    length += 1
                
                longest = max(longest, length)
        
        return longest
        