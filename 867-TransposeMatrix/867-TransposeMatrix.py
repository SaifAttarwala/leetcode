# Last updated: 8/18/2025, 3:14:52 AM
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))
        