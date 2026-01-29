class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False

        while n!=1 and n>1:
            n = n/2
        
        return n==1