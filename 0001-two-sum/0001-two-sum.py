class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            exists = target-nums[i]
            if exists in hashmap:
                return [i, hashmap[exists]]
            hashmap[nums[i]] = i
        