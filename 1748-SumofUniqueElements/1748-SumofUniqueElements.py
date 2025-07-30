# Last updated: 7/31/2025, 12:28:19 AM
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dictionary = Counter(nums)
        unique = []

        for key, val in dictionary.items():
            if val == 1:
                unique.append(key) 
        return sum(unique)