class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        chakkar = time //(n-1)
        
        if chakkar%2 != 0:
            return n - time%(n-1)
        else:
            return time%(n-1) + 1
        