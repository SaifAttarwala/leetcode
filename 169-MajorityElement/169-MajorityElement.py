# Last updated: 8/6/2025, 6:03:37 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = int(len(nums) / 2)
        return nums[n]
        