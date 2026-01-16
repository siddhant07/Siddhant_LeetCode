class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        setter = set()
        repeater = 0
        n = len(grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in setter:
                    repeater = grid[i][j]
                setter.add(grid[i][j])
        
        return [repeater, ((n*n*((n*n)+1))//2)-sum(setter)]
        
        
        