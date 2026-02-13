#Bottom Up dynamic programming

# Let n = cost.length

# Initialize a DP table of size (n + 1) × (n + 1) with all values set to 0

# Set base case: initialize all values in dp[n] to a large number

# Iterate i from n - 1 down to 0

# Iterate remain from 1 to n

# Compute paint = cost[i] + dp[i + 1][max(0, remain - 1 - time[i])]

# Compute dontPaint = dp[i + 1][remain]

# Set dp[i][remain] = min(paint, dontPaint)

# Return dp[0][n]


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            dp[n][i] = inf

        for i in range(n - 1, -1, -1):
            for remain in range(1, n + 1):
                paint = cost[i] + dp[i + 1][max(0, remain - 1 - time[i])]
                dont_paint = dp[i + 1][remain]
                dp[i][remain] = min(paint, dont_paint)
        
        return dp[0][n]
        

# Given n as the length of cost and time,

# Time complexity: O(n**2 )