# Last updated: 8/19/2025, 3:38:24 AM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []

        for x in candies:
            if x + extraCandies >= max(candies):
                res.append(True)
            else:
                res.append(False)
        
        return res