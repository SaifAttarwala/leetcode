# Last updated: 8/16/2025, 7:33:58 AM
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dictionary = Counter(nums)
        unique = []

        for key, val in dictionary.items():
            if val == 1:
                unique.append(key) 
        return sum(unique)