# Last updated: 7/30/2025, 11:54:10 PM
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        while original in nums:
            original *= 2
        return original
        