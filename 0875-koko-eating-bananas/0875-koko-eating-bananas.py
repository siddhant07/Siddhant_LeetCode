import math
class Solution:
    
    def trySpeed(s : int, piles: List[int], h:int) -> int:
        time = 0
        for i in piles:
            time += math.ceil(i/s)
        return time
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r)// 2
            hours = Solution.trySpeed(m, piles, h)
            if hours <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        return res
                
        