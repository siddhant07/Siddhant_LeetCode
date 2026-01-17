class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for k, v in hashmap.items():
            if v == 1:
                return k
        