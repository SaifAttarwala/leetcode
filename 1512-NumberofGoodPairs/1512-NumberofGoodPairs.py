# Last updated: 8/19/2025, 3:43:19 AM
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0

        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[x] == nums[y] and x != y:
                    pairs += 1
        
        return int(pairs/2)
        