# Last updated: 8/11/2025, 4:34:34 AM
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

        