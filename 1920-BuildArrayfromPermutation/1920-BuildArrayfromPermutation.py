# Last updated: 7/27/2025, 6:00:16 AM
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in range(len(nums)):
            ans.append(nums[nums[x]])
        return ans
        