# Last updated: 7/22/2025, 1:05:37 AM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
