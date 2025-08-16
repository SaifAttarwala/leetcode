# Last updated: 8/17/2025, 1:50:32 AM
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0

        for x in grid:
            x.sort()
        
        grid = list(zip(*grid))

        for x in grid:
            res += max(x)
            
        return res