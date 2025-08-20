# Last updated: 8/20/2025, 5:50:08 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [x * x for x in nums]
        nums.sort()
        return nums
        