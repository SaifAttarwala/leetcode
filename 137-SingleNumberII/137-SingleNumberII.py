# Last updated: 8/25/2025, 12:30:12 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = Counter(nums)

        for key, val in nums.items():
            if val == 1:
                return key