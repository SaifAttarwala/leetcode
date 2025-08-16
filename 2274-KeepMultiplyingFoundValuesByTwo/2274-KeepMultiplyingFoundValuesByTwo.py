# Last updated: 8/16/2025, 7:33:49 AM
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        while original in nums:
            original *= 2
        return original
        