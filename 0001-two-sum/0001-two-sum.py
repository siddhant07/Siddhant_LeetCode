class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = set()
        
        for i in range(0, len(nums)):
            if target-nums[i] in hashset:
                return [nums.index(target-nums[i]), i]
            elif nums[i] not in hashset:
                hashset.add(nums[i])
        return 0