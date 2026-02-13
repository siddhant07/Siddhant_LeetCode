# The ball does not stop at each cell, it rolls continuously until hitting a wall.
# We can only consider positions where the ball naturally stops after hitting a wall.

# We use Depth-First Search (DFS) to explore all reachable stopping positions from the start until we reach the destination or determine it is unreachable.

# Algorithm

# Keep a visited set to avoid revisiting stop positions

# Use 4 directions: right, left, down, up

# Run DFS from the start position

# If current position is already visited, return false

# Mark current position as visited

# If current position is the destination, return true

# For each direction, “roll” the ball until the next move would hit a wall or go out of bounds

# Stop at the last valid cell and DFS from that stopping cell

# If any DFS path reaches the destination, return true; otherwise return false

# A cell is valid if it’s inside bounds and equals 0 (empty)

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        y, x = start
        j, i = destination
        
        dirs = [
            [0, 1], [0, -1],
            [1, 0], [-1, 0]
        ]
        
        visited = set()
        
        def in_bounds(mat, y, x):
            return (0 <= y < len(mat) and 
                    0 <= x < len(mat[0]) and 
                    mat[y][x] == 0)
        
        def dfs(y, x):
            key = (y, x)
            
            if key in visited:
                return False
            
            visited.add(key)
            
            if y == j and x == i:
                return True
            
            for dy, dx in dirs:
                y2, x2 = y, x
                
                while in_bounds(maze, y2 + dy, x2 + dx):
                    y2 += dy
                    x2 += dx
                
                if dfs(y2, x2):
                    return True
            
            return False
        
        return dfs(y, x)

# Time Complexity: O(m×n×max(m,n))
        