# Last updated: 03/09/2025, 02:53:01
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sorted(nums).index(i) for i in nums]