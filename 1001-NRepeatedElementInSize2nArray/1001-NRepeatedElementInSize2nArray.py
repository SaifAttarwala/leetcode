# Last updated: 8/24/2025, 11:55:20 PM
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return(list(Counter(nums).most_common())[0][0])
        