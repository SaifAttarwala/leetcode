# Last updated: 8/16/2025, 7:34:05 AM
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        temp = 0
        for x in arr:
            if temp == 3:
                return True
            if x % 2 != 0:
                temp += 1
            else:
                temp = 0
        if temp == 3:
            return True
        return False

        