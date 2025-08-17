# Last updated: 8/18/2025, 4:02:03 AM
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0

        for x in grid:
            x.sort()
        
        grid = list(zip(*grid))

        for x in grid:
            res += max(x)
            
        return res