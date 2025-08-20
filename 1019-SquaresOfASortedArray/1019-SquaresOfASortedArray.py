# Last updated: 8/20/2025, 5:52:26 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x * x for x in nums])
        