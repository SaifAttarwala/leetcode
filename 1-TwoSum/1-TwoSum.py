# Last updated: 7/22/2025, 1:05:44 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for x in range(len(nums)):
            for y in range(1,len(nums)):
                if x == y:
                    pass
                elif nums[x] + nums[y] == target:
                    return x,y
                else:
                    pass
        