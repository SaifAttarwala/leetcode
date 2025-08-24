# Last updated: 8/24/2025, 11:55:06 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res, temp = 0, 0

        for x in gain:
            temp += x
            if temp > res:
                res = temp
        return res