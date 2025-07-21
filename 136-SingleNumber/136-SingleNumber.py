# Last updated: 7/22/2025, 1:36:42 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2* sum(set(nums)) - sum(nums)