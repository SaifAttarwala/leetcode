# Last updated: 7/27/2025, 4:55:30 AM
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)
        else:
            nums.pop()
            nums.pop()
            return max(nums)
        
        
        