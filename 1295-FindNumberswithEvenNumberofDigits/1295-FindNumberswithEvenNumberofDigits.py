# Last updated: 8/20/2025, 4:54:50 AM
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0

        for x in nums:
            if len(str(x)) % 2 == 0:
                res += 1
        return res
        