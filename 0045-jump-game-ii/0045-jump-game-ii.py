#This problem uses Greedy + BFS-style range expansion.

# Initialize near = 0, far = 0, and jumps = 0

# While far is less than the last index:

# Track the farthest reachable index within the range [near, far]

# For each index in this range, compute i + nums[i] and take the maximum

# Update near = far + 1 and far = farthest

# Increment jumps

# Stop when far reaches or passes the last index

# Return jumps

class Solution:
    def jump(self, nums: List[int]) -> int:
        near = far = jumps = 0

        while far < len(nums) - 1:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            
            near = far + 1
            far = farthest
            jumps += 1
        
        return jumps
        
# Time Complexity: O(n)