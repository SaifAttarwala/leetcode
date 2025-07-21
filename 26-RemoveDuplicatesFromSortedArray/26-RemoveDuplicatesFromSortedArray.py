# Last updated: 7/22/2025, 1:05:39 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        
        return len(nums)
        
