# Last updated: 8/19/2025, 4:07:56 AM
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0

        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[x] == nums[y] and x != y:
                    pairs += 1
        
        return int(pairs/2)
        