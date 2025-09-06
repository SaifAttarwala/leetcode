# Last updated: 06/09/2025, 20:47:25
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        temp = 0

        for x in range(len(nums)):
            if nums[x] == 0:
                res = max(res, temp)
                temp = 0
            else:
                temp += 1
        
        return max(res, temp)