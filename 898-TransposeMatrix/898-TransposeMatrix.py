# Last updated: 8/18/2025, 4:02:19 AM
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))
        