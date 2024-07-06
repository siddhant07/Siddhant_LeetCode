class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        time //(n-1)
        
        if (time //(n-1))%2 != 0:
            return n - time%(n-1)
        else:
            return time%(n-1) + 1
        