# Last updated: 7/27/2025, 5:30:39 AM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out =[]
        tot = 0
        for x in range(len(nums)):
            tot = tot + nums[x] 
            out.append(tot)
        return out