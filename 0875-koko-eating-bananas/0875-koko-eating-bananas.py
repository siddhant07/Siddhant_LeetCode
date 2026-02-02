class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low, high = 1, max(piles)
        res = high

        while low<=high:
            speed = (low+high)//2

            totalTime = 0
            for p in piles:
                totalTime+=math.ceil(float(p)/speed)
            
            if totalTime <= h:
                res = speed
                high = speed - 1
            else:
                low = speed + 1
        return res

        