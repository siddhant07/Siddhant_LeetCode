#Approach 2: Bottom-Up Dynamic Programming (Tabulation)

# Create an array totalWays of size n + 1

# Initialize totalWays[1] = k and totalWays[2] = k * k

# For i from 3 to n, compute totalWays[i] = (k - 1) * (totalWays[i - 1] + totalWays[i - 2])

# Return totalWays[n]

class Solution:
    def numWays(self, n: int, k: int) -> int:
        # Base cases for the problem to avoid index out of bound issues
        if n == 1:
            return k
        if n == 2:
            return k * k

        total_ways = [0] * (n + 1)
        total_ways[1] = k
        total_ways[2] = k * k
        
        for i in range(3, n + 1):
            total_ways[i] = (k - 1) * (total_ways[i - 1] + total_ways[i - 2])
        
        return total_ways[n]

    # Time complexity: O(n)
        