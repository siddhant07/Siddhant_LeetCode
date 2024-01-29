class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for i in count:
            frequency[count[i]].append(i)
        
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if(len(res)==k):
                    return res
        
        