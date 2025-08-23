# Last updated: 8/24/2025, 12:25:49 AM
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []

        for x in range(len(index)):
            res.insert(index[x],nums[x])
        
        return res
        