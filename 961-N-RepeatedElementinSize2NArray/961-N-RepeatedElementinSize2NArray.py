# Last updated: 8/20/2025, 11:27:23 PM
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return(list(Counter(nums).most_common())[0][0])
        