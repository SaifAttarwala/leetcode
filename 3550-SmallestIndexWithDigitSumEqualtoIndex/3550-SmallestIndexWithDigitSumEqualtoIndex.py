# Last updated: 8/24/2025, 11:54:37 PM
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for x in range(len(nums)):
            if sum(map(int,str(nums[x]))) == x:
                return x
        return -1

        
        