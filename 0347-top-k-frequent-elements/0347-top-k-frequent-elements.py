class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = [[] for i in range(len(nums)+1)]
        hashset = {}
        #print(counter)
        for n in nums:
            hashset[n] = 1 + hashset.get(n, 0)
        
        #print(hashset)
        
        for val, count in hashset.items():
            #print(val,count)
            counter[count].append(val)
            #print(counter)
        
        print(counter)
        res = []
        
        for i in range(len(counter)-1, 0, -1):
            for n in counter[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
            
        
        