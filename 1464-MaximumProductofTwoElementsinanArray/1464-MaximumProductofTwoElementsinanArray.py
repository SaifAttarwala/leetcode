# Last updated: 8/16/2025, 6:09:39 AM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        x = nums[nums.index(max(nums))] - 1
        nums1 = nums
        nums1.remove(max(nums1))
        y = nums[nums.index(max(nums1))] - 1

        return x * y
        