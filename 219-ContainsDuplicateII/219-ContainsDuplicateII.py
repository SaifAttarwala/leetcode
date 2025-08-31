# Last updated: 9/1/2025, 12:53:16 AM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}

        for i, num in enumerate(nums):
            if num in dic and i-dic[num] <= k:
                return True
            dic[num] = i
        return False
        