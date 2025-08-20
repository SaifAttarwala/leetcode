# Last updated: 8/20/2025, 5:52:19 AM
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] < 0:
                    res +=1
        return res
        