# Last updated: 7/22/2025, 2:09:31 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maximum = max(nums)
        nums.sort()
        i = 0
        
        while i < len(nums):
            if i == len(nums)-1 and i==nums[i]:
                return nums[i]+1
            if i != nums[i]:
                return nums[i]-1
            i += 1
            
        