# Last updated: 7/29/2025, 6:48:09 PM
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in range(len(nums)):
            ans.append(nums[nums[x]])
        return ans
        